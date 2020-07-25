def dumps(d, float_fmt=None):
    sd = _dict_to_strings(d, float_fmt)

    # convert string dict to a single string
    return "{" + ", ".join([f"{key}: {value}" for key, value in sd.items()]) + "}"


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
