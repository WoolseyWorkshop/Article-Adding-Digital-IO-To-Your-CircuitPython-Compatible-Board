"""Controls digital inputs added with a 74HC165 shift register.

Description
-----------

A CircuitPython program that interfaces a 74HC165 parallel-in serial-out shift
register IC to add digital inputs to a CircuitPython compatible board.

Circuit
-------

- A 74HC165 shift register IC is connected to the board's SPI serial bus and D5
  pins.
    - The SPI SCK pin is connected to the 74HC165 CLK (2) pin.
    - The SPI MISO pin is connected to the 74HC165 QH (9) pin.
    - The D5 pin is connected to the 74HC165 SH/LD (1) pin.
    - 8 switches, with pull-down resistors, are connected to the 74HC165's input
      pins (A - H).

Libraries/Modules
-----------------

- time Standard Library
    - https://docs.python.org/3/library/time.html
    - Access to time function.
- board CircuitPython Core Module
    - https://circuitpython.readthedocs.io/en/latest/shared-bindings/board/
    - Access to board's GPIO pins and hardware.
- digitalio CircuitPython Core Module
    - https://circuitpython.readthedocs.io/en/latest/shared-bindings/digitalio/
    - Provides basic digital pin I/O support.
- WoolseyWorkshop_CircuitPython_74HC165 CircuitPython Driver Library
    - https://woolseyworkshop-circuitpython-74hc165.readthedocs.io
    - Provides support for 74HC165 shift register IC.

Notes
-----

- Provides examples for multiple approaches of visualizing and reading digital
  input data from the 74HC165 shift register IC.
- This program assumes a single 74HC165 shift register IC is being utilized.
  If two or more '165s are daisy chained together, change the
  SHIFT_REGISTERS_NUM constant to the actual number of '165s being used.
- Input values are printed to the console.
- Comments are Sphinx (reStructuredText) compatible.

TODO
----

- None.

Author(s)
---------

- Created by John Woolsey on 04/14/2021.
- Modified by John Woolsey on 07/01/2021.

Copyright (c) 2021 Woolsey Workshop.  All rights reserved.

Members
-------
"""


# Imports
from time import time
import board
import digitalio
import wws_74hc165


# Pin Mapping
isr_latch_pin = digitalio.DigitalInOut(board.D5)
"""The pin connected to the 74HC165 SH/LD (1) pin, used for latching data."""


# Global Constants
SAMPLE_RATE = 0.2
"""The sensor sampling rate in Hz."""

SHIFT_REGISTERS_NUM = 1
"""The number of daisy chained 74HC165 shift registers."""


# Global Variables
previous_inputs = bytearray(SHIFT_REGISTERS_NUM)
"""The previous input values read from the shift register."""


# Global Instances
isr = wws_74hc165.ShiftRegister74HC165(board.SPI(), isr_latch_pin, SHIFT_REGISTERS_NUM)
"""The instance of the connected 74HC165 shift register IC."""


# Functions
def read_single_inputs():
    """Example code for reading an individual shift register input with each
    read.

    This approach should be the most familiar to CircuitPython users.  It uses
    the same mechanism as reading standard GPIO pin values, but may involve more
    shift operations than other approaches since only one input at a time can
    be read.
    """

    # Input pin definitions (pin references)
    input_a = isr.get_pin(0)
    input_b = isr.get_pin(1)
    input_c = isr.get_pin(2)
    input_d = isr.get_pin(3)
    input_e = isr.get_pin(4)
    input_f = isr.get_pin(5)
    input_g = isr.get_pin(6)
    input_h = isr.get_pin(7)

    # Read and print individual inputs
    print(f"Input A = {input_a.value}")
    print(f"Input B = {input_b.value}")
    print(f"Input C = {input_c.value}")
    print(f"Input D = {input_d.value}")
    print(f"Input E = {input_e.value}")
    print(f"Input F = {input_f.value}")
    print(f"Input G = {input_g.value}")
    print(f"Input H = {input_h.value}")
    print()


def read_inputs_with_binary_values():
    """Example code for reading all shift register inputs with each read using
    binary values (1 = True, 0 = False).

    This approach produces the most concise code, but does not indicate the
    meaning of each of the inputs.
    """

    # Read and print all inputs, separated in bytes, from shift register in binary format
    print("Inputs: ", end="")
    for byte in isr.gpio:
        print(f"{byte:08b}", end=" ")  # print the current byte in binary format
    print()


def bit_read(data, position):
    """Returns the value of a single bit in a number.

    :param: data     The number (bytearray) that contains the desired bit.
    :param: position The position of the bit in the number.

    :return: The bit value (True or False).
    """

    byte_pos = int(position // 8)  # byte position in number
    bit_pos = int(position % 8)    # bit position in byte
    return bool((data[byte_pos] & (1 << bit_pos)) >> bit_pos)


def read_inputs_with_defined_names():
    """Example code for reading all shift register inputs with each read and
    accessing individually named inputs using bit operations.

    This approach provides named inputs and less shift register reads, but
    requires a variable to hold input values.
    """

    # Input pin definitions (bit positions)
    input_a = 0
    input_b = 1
    input_c = 2
    input_d = 3
    input_e = 4
    input_f = 5
    input_g = 6
    input_h = 7

    # Read all inputs from shift register
    inputs = isr.gpio

    # Read and print individual inputs
    print(f"Input A = {bit_read(inputs, input_a)}")
    print(f"Input B = {bit_read(inputs, input_b)}")
    print(f"Input C = {bit_read(inputs, input_c)}")
    print(f"Input D = {bit_read(inputs, input_d)}")
    print(f"Input E = {bit_read(inputs, input_e)}")
    print(f"Input F = {bit_read(inputs, input_f)}")
    print(f"Input G = {bit_read(inputs, input_g)}")
    print(f"Input H = {bit_read(inputs, input_h)}")
    print()


def read_and_print_inputs_on_change():
    """Example code for reading all shift register inputs in a single read and
    printing all values, separated into bytes, when an input change is detected.
    """

    global previous_inputs
    current_inputs = isr.gpio  # read all inputs from shift register
    if current_inputs != previous_inputs:  # print values only if they changed
        print("Inputs: ", end="")
        for byte in current_inputs:
            print(f"{byte:08b}", end=" ")  # print the current byte in binary format
        print()
        previous_inputs = current_inputs[:]  # save (copy) current inputs for next comparison


def main():
    """Main program entry."""

    # Read and print inputs at the specified sampling rate
    previous_time = time()  # time in seconds
    while True:
        current_time = time()  # time in seconds
        if current_time - previous_time >= 1.0 / SAMPLE_RATE:
            read_single_inputs()
            # read_inputs_with_binary_values()
            # read_inputs_with_defined_names()
            previous_time = current_time

    # Read inputs and print values upon any change
    # while True:
    #     read_and_print_inputs_on_change()


if __name__ == "__main__":  # required for generating Sphinx documentation
    main()
