# Analysis Notes

## Current status

- The 2 MB input is a Dell Linux DUP wrapper.
- It contains payload/095HR5_190AD_00.3D.67.bin.
- The payload has a 67-byte vendor header.
- Starting at payload offset 0x104, the data has repeated 4-byte records whose first byte is normally 0x00 and whose remaining 3 bytes have the appearance of 24-bit dsPIC/PIC24 instruction words.
- This is a hypothesis to be validated with Ghidra dsPIC33E decoding.

## Target functions

I2C/PMBus RX/TX
command dispatch
READ_VOUT
VOUT_COMMAND
OCP / current limit
OVP / UVP
ADC sampling
PWM/reference control
fault latch
thermal protection
fan control
EEPROM/configuration
