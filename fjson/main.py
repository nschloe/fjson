def dumps(d, float_fmt=None, indent=None):
    sd = _dict_to_strings(d, float_fmt)

    # convert string dict to a single string
    if indent is None:
        return "{" + ", ".join([f"{key}: {value}" for key, value in sd.items()]) + "}"

    return _dict_to_string(sd, indent)


def _dict_to_string(sd, indent, level=1):
    out = ""
    out += "{\n"
    length = len(sd)
    for k, (key, value) in enumerate(sd.items()):
        if isinstance(value, dict):
            out += _dict_to_string(value, indent, level + 1)
        else:
            out += (level * indent) * " " + f"{key}: {value}"

        if k < length - 1:
            out += ","

        out += "\n"

    out += "}"
    return out


def _dict_to_strings(d, float_fmt):
    # convert everything to strings
    out = {}
    for key, value in d.items():
        assert isinstance(key, str)
        k = _tostring_str(key)

        if isinstance(value, dict):
            out[k] = _dict_to_strings(value, float_fmt)
        elif isinstance(value, str):
            out[k] = _tostring_str(value)
        elif isinstance(value, int):
            out[k] = _tostring_int(value)
        elif isinstance(value, float):
            out[k] = _tostring_float(value, float_fmt)
        else:
            raise ValueError(f"Don't know how to handle entry with key {key}.")
    return out


def _tostring_str(string):
    return f"\"{string}\""


def _tostring_int(val):
    return str(val)


def _tostring_float(val, fmt):
    if fmt is None:
        return str(val)
    return f"{val:{fmt}}"
