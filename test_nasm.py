#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path
import math

import pytest
import yaml

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)


def text_to_ram(text, offset=0):
    ram = {}
    for i in range(len(text)):
        ram[i + offset] = ord(text[i])
    return ram


@pytest.mark.telemetry_files(source("abs.nasm"))
def test_abs():
    ram = {1: -1}
    tst = {0: 1}
    assert nasm_test("abs.nasm", ram, tst)

    ram = {1: 35}
    tst = {0: 35}
    assert nasm_test("abs.nasm", ram, tst)


@pytest.mark.telemetry_files(source("mod.nasm"))
def test_mod():
    ram = {0: 0, 1: 0}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 0, 1: 5}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 32, 1: 5}
    tst = {2: 2}
    assert nasm_test("mod.nasm", ram, tst, 10000)

    ram = {0: 1023, 1: 7}
    tst = {2: 1}
    assert nasm_test("mod.nasm", ram, tst, 10000)


@pytest.mark.telemetry_files(source("isEven.nasm"))
def test_isEven():
    ram = {0: 2, 5: 64}
    tst = {0: 1}
    assert nasm_test("isEven.nasm", ram, tst)

    ram = {0: 2, 5: 1023}
    tst = {0: 0}
    assert nasm_test("isEven.nasm", ram, tst)


@pytest.mark.telemetry_files(source("isOdd.nasm"))
def test_isOdd():
    ram = {0: 1, 5: 64}
    tst = {0: 0}
    assert nasm_test("isOdd.nasm", ram, tst)

    ram = {0: 2, 5: 1023}
    tst = {0: 1}
    assert nasm_test("isOdd.nasm", ram, tst)


@pytest.mark.telemetry_files(source("numberOf4.nasm"))
def test_numberOf4():
    ram = {0: 0, 5: 0, 16: 0, 18: 0, 22: 0, 27: 0, 31: 0}
    tst = {32: 0}
    assert nasm_test("numberOf4.nasm", ram, tst)

    ram = {0: 0, 5: 4, 16: 2, 18: 4, 22: 4, 27: 0, 31: 4}
    tst = {32: 4}
    assert nasm_test("numberOf4.nasm", ram, tst)


@pytest.mark.telemetry_files(source("numberOfx.nasm"))
def test_numberOfx():
    ram = {0: 0, 5: 2, 16: 0, 18: 0, 22: 0, 27: 0, 31: 0, 32: 1}
    tst = {33: 0}
    assert nasm_test("numberOfx.nasm", ram, tst)

    ram = {0: 9, 5: 4, 16: 2, 18: 4, 22: 4, 27: 9, 31: 9, 32: 9}
    tst = {33: 3}
    assert nasm_test("numberOfx.nasm", ram, tst)


@pytest.mark.telemetry_files(source("stringLength.nasm"))
def test_stringLenght():
    ram = {}
    text = "oi tudo bem?"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)

    text = "o saci eh um ser muito especial"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)


@pytest.mark.telemetry_files(source("palindromo.nasm"))
def test_palindromo():
    ram = text_to_ram("ararr", 10)
    ram[0] = 2
    tst = {0: 0}
    assert nasm_test("palindromo.nasm", ram, tst, 10000)

    ram = text_to_ram("arara", 10)
    ram[0] = 2
    tst = {0: 1}
    print(ram)
    assert nasm_test("palindromo.nasm", ram, tst, 10000)

@pytest.mark.telemetry_files(source("vectorFill.nasm"))
def test_vectorFill_example():
    ram = {3: 7, 4: 4}
    tst = {}
    for i in range(ram[4]):
        tst[5 + i] = ram[3]
    assert nasm_test("vectorFill.nasm", ram, tst, 5000)


@pytest.mark.telemetry_files(source("vectorFill.nasm"))
def test_vectorFill_generic():
    ram = {3: 32, 4: 55}
    tst = {}
    for i in range(ram[4]):
        tst[5 + i] = ram[3]
    assert nasm_test("vectorFill.nasm", ram, tst, 5000)
