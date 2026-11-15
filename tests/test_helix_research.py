"""Tests for HELIX-Research: spiral memory with parity."""

import pytest

from helix_research import HelixMemory, spiral_coordinates


def test_spiral_coordinates_start_center_cover_all():
    coords = spiral_coordinates(3)
    assert coords[0] == (1, 1)
    assert len(coords) == 9
    assert len(set(coords)) == 9
    with pytest.raises(ValueError):
        spiral_coordinates(0)


def test_write_then_read_record_roundtrip():
    memory = HelixMemory(size=8, record_size=4)
    memory.write("alpha", b"")
    assert memory.read_record("alpha") == b""
    assert memory.read_cell("alpha") == 1


def test_write_validates_length():
    memory = HelixMemory(size=8, record_size=4)
    with pytest.raises(ValueError):
        memory.write("a", b"too long")
    with pytest.raises(ValueError):
        memory.write("a", b"short")


def test_verify_true_after_writes():
    memory = HelixMemory(size=8, record_size=4)
    memory.write("alpha", b"")
    memory.write("beta", b"	")
    assert memory.verify() is True


def test_corrupt_is_detected_by_verify():
    memory = HelixMemory(size=8, record_size=4)
    memory.write("alpha", b"")
    memory.corrupt("alpha")
    assert memory.verify() is False


def test_usage_and_len():
    memory = HelixMemory(size=8, record_size=4)
    memory.write("alpha", b"")
    assert len(memory) == 1
    assert memory.usage() == pytest.approx(1 / 64)
