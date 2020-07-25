import math
import json

import fjson


def test_simple():
    a = {"a": 1, "b": math.pi, "c": ["x", "y", {"z": 5}], "d": {"r": 5, "s": [2, 3]}}
    ref = json.dumps(a)
    print(ref)
    string = fjson.dumps(a)
    print(string)
    assert ref == string


def test_indent():
    a = {"a": 1, "b": math.pi, "c": ["x", "y", "z"], "d": {"r": 5, "s": 7}}
    ref = json.dumps(a, indent=2)
    string = fjson.dumps(a, indent=2)
    assert ref == string


def test_format():
    a = {"a": 1, "b": math.pi}
    string = fjson.dumps(a, float_fmt=".6e")
    assert string == '{"a": 1, "b": 3.141593e+00}'
