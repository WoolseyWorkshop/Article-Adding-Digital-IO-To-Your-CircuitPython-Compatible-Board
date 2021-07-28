"""Controls digital inputs and outputs added with an MCP23017 IC.

Description
-----------

A CircuitPython program that interfaces an MCP23017 16-Bit I2C I/O Expander With
Serial Interface IC to add digital inputs and outputs to a CircuitPython
compatible board.

Circuit
-------

- An MCP23017 I/O expander IC is connected to the board's I2C serial bus and D5
  pins.
    - The I2C SCL pin is connected to the MCP23017 SCK (12) pin.
    - The I2C SDA pin is connected to the MCP23017 SDA (13) pin.
    - The D5 pin is connected to the MCP23017 INTB (19) pin.
    - 8 LEDs are connected, via resistors, to the MCP23017 GPA0-GPA7 (21-28)
      pins.
    - 8 switches, with pull-down resistors, are connected to the MCP23017
      GPB0-GPB7 (1-8) pins.

Libraries/Modules
-----------------

- board CircuitPython Core Module
    - https://circuitpython.readthedocs.io/en/latest/shared-bindings/board/
    - Access to board's GPIO pins and hardware.
- digitalio CircuitPython Core Module
    - https://circuitpython.readthedocs.io/en/latest/shared-bindings/digitalio/
    - Provides basic digital pin I/O support.
- Adafruit_CircuitPython_MCP230xx CircuitPython Driver Library
    - https://circuitpython.readthedocs.io/projects/mcp230xx/
    - Provides support for MCP23017 I/O expander IC.

Notes
-----

- Provides examples for multiple approaches to configuring and using digital
  I/O with the MCP23017 I/O expander IC.
- Comments are Sphinx (reStructuredText) compatible.

TODO
----

- None.

Author(s)
---------

- Created by John Woolsey on 07/08/2021.
- Modified by John Woolsey on 07/27/2021.

Copyright (c) 2021 Woolsey Workshop.  All rights reserved.

Members
-------
"""


# Imports
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_mcp230xx.mcp23017 import MCP23017


# Pin Mapping
mcp23017_intb = DigitalInOut(board.D5)
"""The pin connected to the MCP23017 INTB (19) pin."""


# Global Constants
MCP23017_I2C_ADDRESS = 0x20
"""The I2C address of the MCP23017 IC."""


# Global Variables
leds = []
"""Refers to the LEDs connected to the GPA0-GPA7 (21-28) pins of the MCP23017."""

switches = []
"""Refers to the switches connected to the GPB0-GPB7 (1-8) pins of the MCP23017."""


# Global Instances
mcp23017 = MCP23017(board.I2C(), address=MCP23017_I2C_ADDRESS)
"""The instance of the connected MCP23017 IC."""


# Functions
def configure_pins():
    """Configures MCP23017 I/O pins using familiar pin configuration methods.

    Provides two alternatives for configuring pins:
        1. Explicit setting of pin attributes, or
        2. Use of the switch_to_input() and switch_to_output() methods.
    """

    # LEDs - MCP23017 Port A (pins 0-7)
    for pin in range(0, 8):
        leds.append(mcp23017.get_pin(pin))
    for led in leds:
        # Set attributes explicitly
        # led.direction = Direction.OUTPUT
        # led.value = False

        # Use switch_to_output() method
        led.switch_to_output(value=False)

    # Switches - MCP23017 Port B (pins 8-15)
    for pin in range(8, 16):
        switches.append(mcp23017.get_pin(pin))
    for switch in switches:
        # Set attributes explicitly
        # switch.direction = Direction.INPUT
        # switch.pull = Pull.UP
        # switch.invert_polarity = True

        # Use switch_to_input() method
        switch.switch_to_input(pull=Pull.UP, invert_polarity=True)


def configure_ports():
    """Configures MCP23017 I/O pins using port configuration methods.

    Provides two alternatives for configuring ports:
        1. Set attributes for individual ports, or
        2. Set attributes for combined ports.
    """

    # Configure port A and port B separately
    # mcp23017.iodira = 0b00000000  # set all port A pins (LEDs) as outputs
    # mcp23017.iodirb = 0b11111111  # set all port B pins (switches) as inputs
    # mcp23017.gppub = 0b11111111   # enable pull-ups on all port B pins (switches)
    # mcp23017.ipolb = 0b11111111   # invert polarity on all port B pins (switches)

    # Configure combined ports
    mcp23017.iodir = 0xFF00  # set port A pins (LEDs) as outputs and port B pins (switches) as inputs
    mcp23017.gppu = 0xFF00   # enable pull-ups on port B pins (switches) only
    mcp23017.ipol = 0xFF00   # invert polarity on port B pins (switches) only


def configure_interrupts():
    """Configures and enables MCP23017 interrupts on port B."""

    mcp23017_intb.direction = Direction.INPUT
    mcp23017_intb.pull = Pull.UP
    mcp23017.interrupt_enable = 0xFF00  # enable interrupts on port B pins (switches) only
    mcp23017.interrupt_configuration = 0x0000  # compare pins against previous values
    mcp23017.clear_ints()  # clear all interrupts


def read_and_write_pin():
    """Example code for reading and writing individual inputs and outputs.

    This approach should be the most familiar to CircuitPython users.  It uses
    the same mechanisms as reading and setting standard GPIO pin values, but may
    involve more operations than other approaches since only one input or output
    at a time can be read or written.
    """

    for pin, switch in enumerate(switches):
        if switch.value:
            leds[pin].value = True
        else:
            leds[pin].value = False


def port_copy():
    """Example code for reading all inputs of port B in a single read and
    setting all outputs of port A with a single write.

    This approach produces the most concise code, but does not indicate the
    meaning of each of the inputs or outputs.
    """

    mcp23017.gpioa = mcp23017.gpiob


def read_and_write_port_on_input_change():
    """Example code using interrupts to determine when an input pin has changed
    and then performs a simple copy from port B (switches) to port A (LEDs).

    This approach should be used when inputs are not expected to change rapidly
    and a full port copy will suffice.  It allows the microcontroller to spend
    more time on other tasks.

    Note: CircuitPython does not currently support GPIO interrupts, so interrupt
    pin polling is implemented instead.
    """

    if not mcp23017_intb.value:  # active low
        port_copy()  # copy port B (switches) values to port A (LEDs)
        mcp23017.clear_ints()  # clear all interrupts


def read_and_write_pin_on_input_change():
    """Example code using interrupts to determine when an input pin has
    changed, captures which pin caused the interrupt along with its associated
    value, and then updates the appropriate LED pin with the switch's new value.

    This approach should be used when inputs are not expected to change rapidly
    and the changed pin's position and value are desired.  It allows the
    microcontroller to spend more time on other tasks.

    Note: CircuitPython does not currently support GPIO interrupts, so interrupt
    pin polling is implemented instead.
    """

    if not mcp23017_intb.value:  # active low
        flagb = mcp23017.int_flagb  # retrieves which pin(s) caused the interrupt
        capb = mcp23017.int_capb  # retrieves pin values captured at time of interrupt
        for pin in flagb:
            leds[pin - 8].value = capb[pin - 8]  # set LED output value to captured switch input value
        mcp23017.clear_ints()  # clear all interrupts


# Main
# configure_pins()
configure_ports()
# configure_interrupts()

while True:
    # read_and_write_pin()
    port_copy()
    # read_and_write_port_on_input_change()
    # read_and_write_pin_on_input_change()
