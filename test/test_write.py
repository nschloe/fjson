import math
import json

import fjson


def test_dumps():
    a = {"a": 1, "b": math.pi}
    ref = json.dumps(a)
    string = fjson.dumps(a)
    assert ref == string
