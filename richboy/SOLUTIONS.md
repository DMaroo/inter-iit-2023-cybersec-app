# richboy

## File format

The given file is a GameBoy ROM.

```
$ file treasure
treasure: Game Boy ROM image (Rev.00) [ROM ONLY], ROM: 256Kbit
```

## ROM format

GameBoy ROM header format: https://gbdev.io/pandocs/The_Cartridge_Header

Change the `0x00` byte at offset `0x100` (0-indexed) to `0xc3`.

## Running

Run the ROM on any GameBoy emulator. You will get the following screen.

![flag](./flag.png)
