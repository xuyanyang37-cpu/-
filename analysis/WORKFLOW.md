# Full reverse-engineering workflow

## 1. Preserve inputs

Keep the original Dell DUP and extracted payload read-only. Record SHA-256 for every derived artifact.

## 2. Confirm image format

Validate the 67-byte payload header and 4-byte record layout. Do not assume the apparent packed 24-bit words are executable until the disassembler confirms valid instruction sequences and vectors.

## 3. Ghidra

1. Install a current Ghidra release.
2. Confirm the PIC processor module includes dsPIC33E language support. Ghidra's language definition identifies dsPIC33E as PIC-24 and includes PIC24.sinc.
3. Import the correctly unpacked instruction image, not the DUP wrapper.
4. Select the matching dsPIC33E language and correct memory/address mapping.
5. Define reset and interrupt vectors only after validating their locations.
6. Run analysis; inspect invalid instructions, function boundaries, references, and data/code overlap.
7. Export disassembly, function list, call graph, and decompiler output.

## 4. Protocol recovery

Start from peripheral initialization and interrupt handlers. Trace I2C state machines, receive/transmit buffers, command dispatch, checksums/PEC, and response paths. Then cross-reference telemetry values to ADC/scaling routines and protection thresholds.

## 5. Pseudocode quality

Every recovered function should include:
- address and size
- confidence (confirmed / likely / speculative)
- callers and callees
- referenced RAM/SFR addresses
- protocol or protection role
- evidence notes

## 6. Safety

Never test unknown writes against a powered high-energy PSU. Validate protocol hypotheses offline first.
