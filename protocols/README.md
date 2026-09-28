# Protocol inventory

This is an evidence ledger, not a claim that every protocol has already been recovered.

| Protocol / interface | Evidence | Status | Next verification |
|---|---|---|---|
| PMBus / SMBus over I2C | User has observed address 0x58 and telemetry reads | Observed, command map incomplete | Capture transactions; identify PEC, framing, supported commands |
| I2C/SMBus vendor commands | Possible in PSU management firmware | Unconfirmed | Trace command dispatch and compare bus captures |
| ICSP programming interface | dsPIC33FJ64GS606 devices identified on board | Physical access not yet mapped | Identify PGEC/PGED/VDD/VSS/MCLR pins from datasheet and board |
| Internal control/ADC/PWM signals | UCC28950 and dsPIC devices reported on board | Functional ownership unconfirmed | Trace nets and correlate firmware peripheral setup |
| External EEPROM/Flash protocol | No chip confirmed in this ledger | Unknown | Board photo / chip marking / continuity inspection |
| Dell DUP update container | Official Linux DUP package extracted | Confirmed container format | Document payload/header and update manifest |

## Command families to investigate

- Standard PMBus telemetry: READ_VOUT, READ_IOUT, READ_TEMPERATURE_1, READ_FAN_SPEED_1, STATUS_WORD
- Configuration/write candidates: VOUT_COMMAND, VOUT_MAX, VOUT_MARGIN_HIGH/LOW, IOUT_OC_FAULT_LIMIT, IOUT_OC_WARN_LIMIT, VOUT_OV_FAULT_LIMIT, VOUT_UV_FAULT_LIMIT
- Vendor-specific commands: unknown until command dispatcher is recovered

Do not issue writes to a live PSU during discovery. A command's existence in the PMBus standard does not prove this firmware implements it.
