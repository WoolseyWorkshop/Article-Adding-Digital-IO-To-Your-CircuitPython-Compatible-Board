"""Controls digital outputs added with a 74HC595 shift register.

Description
-----------

A CircuitPython program that interfaces a 74HC595 serial-in parallel-out shift
register IC to add digital outputs to a CircuitPython compatible board.

Circuit
-------

- A 74HC595 shift register IC is connected to the board's SPI serial bus and D5
  pins.
    - The SPI SCK pin is connected to the 74HC595 SRCLK (11) pin.
    - The SPI MOSI pin is connected to the 74HC595 SER (14) pin.
    - The D5 pin is connected to the 74HC595 RCLK (12) pin.
    - 8 LEDs are connected, via resistors, to the 74HC595's output pins
      (QA - QH).

Libraries/Modules
-----------------

- time Standard Library
    - https://docs.python.org/3/library/time.html
    - Access to sleep function.
- board CircuitPython Core Module
    - https://circuitpython.readthedocs.io/en/latest/shared-bindings/board/
    - Access to board's GPIO pins and hardware.
- digitalio CircuitPython Core Module
    - https://circuitpython.readthedocs.io/en/latest/shared-bindings/digitalio/
    - Provides basic digital pin I/O support.
- Adafruit_CircuitPython_74HC595 CircuitPython Driver Library
    - https://circuitpython.readthedocs.io/projects/74hc595/
    - Provides support for 74HC595 shift register IC.

Notes
-----

- Provides examples for multiple approaches of visualizing and sending digital
  output data to the 74HC595 shift register IC.
- This program assumes a single 74HC595 shift register IC is being utilized.
  If two or more '595s are daisy chained together, change the
  SHIFT_REGISTERS_NUM constant to the actual number of '595s being used.
  See function specific comments for additional details.
- Comments are Sphinx (reStructuredText) compatible.

TODO
----

- None.

Author(s)
---------

- Created by John Woolsey on 04/13/2021.
- Modified by John Woolsey on 06/14/2021.

Copyright (c) 2021 Woolsey Workshop.  All rights reserved.

Members
-------
"""


# Imports
from time import sleep
import board
import digitalio
import adafruit_74hc595


# Pin Mapping
osr_latch_pin = digitalio.DigitalInOut(board.D5)
"""The pin connected to the 74HC595 RCLK (12) pin, used for latching data."""


# Global Constants
SHIFT_REGISTERS_NUM = 1
"""The number of daisy chained 74HC595 shift registers."""


# Global Instances
osr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), osr_latch_pin, SHIFT_REGISTERS_NUM)
"""The instance of the connected 74HC595 shift register IC."""


# Functions
def change_single_outputs():
    """Example code for setting an individual shift register output with each
    write.

    This approach should be the most familiar to CircuitPython users.  It uses
    the same mechanism as setting standard GPIO pin values, but may involve more
    shift operations than other approaches since only one output at a time can
    be changed.
    """

    # Output pin definitions (pin references)
    led_0 = osr.get_pin(0)
    led_1 = osr.get_pin(1)
    led_2 = osr.get_pin(2)
    led_3 = osr.get_pin(3)
    led_4 = osr.get_pin(4)
    led_5 = osr.get_pin(5)
    led_6 = osr.get_pin(6)
    led_7 = osr.get_pin(7)

    # Set individual LEDs
    led_1.value = True   # turn on LED 1 only
    sleep(1)
    led_1.value = False  # turn off LED 1 only
    led_6.value = True   # turn on LED 6 only
    sleep(1)
    led_6.value = False  # turn off LED 6 only
    sleep(1)

    # Set multiple LEDs
    led_0.value = True   # turn on even numbered LEDs
    led_2.value = True
    led_4.value = True
    led_6.value = True
    sleep(1)
    led_0.value = False  # turn off even numbered LEDs
    led_2.value = False
    led_4.value = False
    led_6.value = False
    led_1.value = True   # turn on odd numbered LEDs
    led_3.value = True
    led_5.value = True
    led_7.value = True
    sleep(1)
    led_1.value = False  # turn off odd numbered LEDs
    led_3.value = False
    led_5.value = False
    led_7.value = False
    sleep(1)


def change_outputs_with_binary_values():
    """Example code for setting all shift register outputs with each write using
    binary values (1 = True, 0 = False).

    This approach produces the most concise code, but does not indicate the
    meaning of each of the outputs.

    If daisy chaining multiple shift registers together, set the appropriate
    byte (index) of the outputs variable.
    """

    outputs = osr.gpio  # retrieve current shift register output values

    # Set individual LEDs
    outputs[0] = 0b00000010  # turn on LED 1 only
    osr.gpio = outputs       # set new shift register output values
    sleep(1)
    outputs[0] = 0b01000000  # turn on LED 6 only
    osr.gpio = outputs
    sleep(1)
    outputs[0] = 0b00000000  # turn off all LEDs
    osr.gpio = outputs
    sleep(1)

    # Set multiple LEDs
    outputs[0] = 0b01010101  # turn on only even numbered LEDs
    osr.gpio = outputs
    sleep(1)
    outputs[0] = 0b10101010  # turn on only odd numbered LEDs
    osr.gpio = outputs
    sleep(1)
    outputs[0] = 0b00000000  # turn off all LEDs
    osr.gpio = outputs
    sleep(1)


def change_outputs_with_defined_names():
    """Example code for setting all shift register outputs with each write using
    named outputs.

    This approach provides the ability to use named outputs with single shift
    register writes, but all outputs must still be represented with each write.

    Only include named outputs to set True, everything else will be set False.

    If daisy chaining multiple shift registers together, set the appropriate
    byte (index) of the outputs variable.
    """

    # Output pin definitions (bit positions)
    led_0 = 0b00000001
    led_1 = 0b00000010
    led_2 = 0b00000100
    led_3 = 0b00001000
    led_4 = 0b00010000
    led_5 = 0b00100000
    led_6 = 0b01000000
    led_7 = 0b10000000

    outputs = osr.gpio  # retrieve current shift register output values

    # Set individual LEDs
    outputs[0] = led_1  # turn on LED 1 only
    osr.gpio = outputs  # set new shift register output values
    sleep(1)
    outputs[0] = led_6  # turn on LED 6 only
    osr.gpio = outputs
    sleep(1)
    outputs[0] = 0      # turn off all LEDs
    osr.gpio = outputs
    sleep(1)

    # Set multiple LEDs
    outputs[0] = led_0 | led_2 | led_4 | led_6  # turn on only even numbered LEDs
    osr.gpio = outputs
    sleep(1)
    outputs[0] = led_1 | led_3 | led_5 | led_7  # turn on only odd numbered LEDs
    osr.gpio = outputs
    sleep(1)
    outputs[0] = 0                              # turn off all LEDs
    osr.gpio = outputs
    sleep(1)


def cycle_leds():
    """Example code that continuously cycles through the LEDs (end to end)."""

    leds = [osr.get_pin(n) for n in range(8 * osr.number_of_shift_registers)]
    for position, led in enumerate(leds):
        if position == len(leds) - 1: break  # skip the last LED
        led.value = True
        sleep(0.1)
        led.value = False
    for position, led in enumerate(reversed(leds)):
        if position == len(leds) - 1: break  # skip the first LED
        led.value = True
        sleep(0.1)
        led.value = False


def main():
    """Main program entry."""

    while True:
        change_single_outputs()
        change_outputs_with_binary_values()
        change_outputs_with_defined_names()
        # cycle_leds()


if __name__ == "__main__":  # required for generating Sphinx documentation
    main()

