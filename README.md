<p align="center">
  <a href="https://github.com/nschloe/fjson"><img alt="fjson" src="https://nschloe.github.io/fjson/logo.svg" width="50%"></a>
  <p align="center">JSON with float formatting.</p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/fjson.svg?style=flat-square)](https://pypi.org/project/fjson)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/fjson.svg?style=flat-square)](https://pypi.org/pypi/fjson/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/fjson.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/fjson)
[![PyPi downloads](https://img.shields.io/pypi/dm/fjson.svg?style=flat-square)](https://pypistats.org/packages/fjson)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/fjson/ci?style=flat-square)](https://github.com/nschloe/fjson/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/fjson.svg?style=flat-square)](https://codecov.io/gh/nschloe/fjson)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)


The [json](https://docs.python.org/3/library/json.html) module in the Python standard
library does not allow you to specify the format in which `float`s are written out the
file. This module adds the `float_format` parameter.
```python
import math
import fjson


data = {"a": 1, "b": math.pi}
string = fjson.dumps(data, float_format=".6e", indent=2, separators=(", ", ": "))
print(string)
```
<!--pytest-codeblocks:expected-output-->
```json
{
  "a": 1,
  "b": 3.141593e+00
}
```


### License

fjson is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
