from typing import Optional, Tuple


def dump(d, fp, **kwargs):
    fp.write(dumps(d, **kwargs))


def dumps(
    d,
    float_format: Optional[str] = None,
    indent: Optional[int] = None,
    separators: Tuple[str, str] = (", ", ": "),
):
    sd = _dict_to_strings(d, float_format)
    return _dict_to_string(sd, indent, separators)


def _dict_to_string(sd, indent, separators=(", ", ": "), level=1):
    out_lst = []
    length = len(sd)
    for k, (key, value) in enumerate(sd.items()):
        out = "" if indent is None else (level * indent) * " "

        out += f"{key}{separators[1]}"

        out += _value_to_string2(value, indent, separators, level + 1)

        if k < length - 1:
            sep = separators[0]
            if indent is not None:
                sep = sep.rstrip()
            out += sep

        out_lst.append(out)

    if indent is None:
        return "{" + "".join(out_lst) + "}"
    return "{\n" + "\n".join(out_lst) + "\n" + (indent * (level - 1) * " ") + "}"


def _list_to_string(lst, indent, separators, level=1):
    out_lst = []
    length = len(lst)
    for k, value in enumerate(lst):
        out = "" if indent is None else (level * indent) * " "

        out += _value_to_string2(value, indent, separators, level + 1)

        if k < length - 1:
            sep = separators[0]
            if indent is not None:
                sep = sep.rstrip()
            out += sep

        out_lst.append(out)

    if indent is None:
        return "[" + "".join(out_lst) + "]"
    return "[\n" + "\n".join(out_lst) + "\n" + (indent * (level - 1) * " ") + "]"


def _value_to_string2(value, indent, separators, level):
    if isinstance(value, dict):
        return _dict_to_string(value, indent, separators, level=level)
    elif isinstance(value, list):
        return _list_to_string(value, indent, separators, level)
    return f"{value}"


def _value_to_string(value, float_fmt):
    if value is None:
        return _tostring_none(value)
    elif isinstance(value, dict):
        return _dict_to_strings(value, float_fmt)
    elif isinstance(value, list):
        return _list_to_strings(value, float_fmt)
    elif isinstance(value, str):
        return _tostring_str(value)
    elif isinstance(value, bool):
        return _tostring_bool(value)
    elif isinstance(value, int):
        return _tostring_int(value)
    elif isinstance(value, float):
        return _tostring_float(value, float_fmt)

    try:
        # works for numpy arrays
        value = value.tolist()
    except AttributeError:
        pass
    else:
        return _list_to_strings(value, float_fmt)

    raise ValueError(f"Don't know how to handle entry of type {type(value)}.")


def _dict_to_strings(d, float_fmt):
    # convert everything to strings
    out = {}
    for key, value in d.items():
        assert isinstance(key, str)
        k = _tostring_str(key)
        out[k] = _value_to_string(value, float_fmt)
    return out


def _list_to_strings(lst, float_fmt):
    return [_value_to_string(value, float_fmt) for value in lst]


def _tostring_str(string):
    return f'"{string}"'


def _tostring_int(val):
    return str(val)


def _tostring_float(val, fmt):
    if fmt is None:
        return str(val)
    return f"{val:{fmt}}"


def _tostring_bool(val):
    return "true" if val else "false"


def _tostring_none(val):
    return "null"
