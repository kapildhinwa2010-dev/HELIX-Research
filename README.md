# HELIX-Research

[![CI](https://github.com/kapildhinwa2010-dev/HELIX-Research/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/HELIX-Research/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kapildhinwa2010-dev/HELIX-Research/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/HELIX-Research/actions/workflows/codeql.yml)

Research framework for spiral-addressed byte memory with XOR row parity.

## What it does

HelixMemory is a square byte arena addressed by a clockwise spiral walk
from the center. Records are written across consecutive spiral cells
(wrapping at the edge) and each row carries XOR parity, so corruption
with odd parity is detectable by verify().

    from helix_research import HelixMemory

    memory = HelixMemory(size=8, record_size=4)
    memory.write("alpha", b"\x01\x02\x03\x04")
    print(memory.read_record("alpha"))
    print(memory.verify())

## API

- spiral_coordinates(size) - the deterministic spiral walk
- HelixMemory.write / read_record / read_cell / verify / corrupt / usage

## Honest results and limitations

- XOR parity detects odd numbers of flipped bits per row; even flips
  cancel and pass verification. Parity does not locate the bad cell, so
  there is no automatic repair.
- Keys hash to a start index by character sum: different keys can map to
  overlapping cell ranges and silently overwrite each other.
- This is a research toy for the spiral-addressing idea, not storage you
  should trust with data.

## Status

Part of the kapildhinwa2010-dev toolkit experiments. CI and CodeQL run on
every push to main. License: MIT.
