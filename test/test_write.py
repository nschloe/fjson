import json
import math

import numpy
import pytest

import fjson


def test_simple():
    a = {"a": 1, "b": math.pi, "c": ["x", "y", {"z": 5}], "d": {"r": 5, "s": [2, 3]}}
    ref = json.dumps(a)
    string = fjson.dumps(a)
    assert ref == string


@pytest.mark.parametrize("indent", [0, 2])
def test_indent(indent):
    a = {"a": 1, "b": math.pi, "c": ["x", "y", {"z": 5}], "d": {"r": 5, "s": [2, 3]}}
    ref = json.dumps(a, indent=indent)
    string = fjson.dumps(a, indent=indent)
    assert ref == string


def test_format():
    a = {"a": 1, "b": math.pi}
    string = fjson.dumps(a, float_format=".6e")
    assert string == '{"a": 1, "b": 3.141593e+00}'


def test_format2():
    a = {"a": 1, "b": [math.pi, math.e]}
    string = fjson.dumps(a, float_format=".6e")
    assert string == '{"a": 1, "b": [3.141593e+00, 2.718282e+00]}'


def test_numpy():
    a = {"a": numpy.array([1, 2, 3])}
    string = fjson.dumps(a)
    assert string == '{"a": [1, 2, 3]}'
