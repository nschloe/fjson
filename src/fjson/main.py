from __future__ import annotations


def dump(d: dict, fp, **kwargs):
    fp.write(dumps(d, **kwargs))


def dumps(
    d: dict,
    float_format: str | None = None,
    indent: int | None = None,
    separators: tuple[str, str] = (", ", ": "),
):
    sd = _dict_to_strings(d, float_format)
    return _dict_to_string(sd, indent, separators)


def _dict_to_string(
    sd: dict,
    indent: int | None,
    separators: tuple[str, str] = (", ", ": "),
    level: int = 1,
) -> str:
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


def _list_to_string(
    lst: list, indent: int | None, separators: tuple[str, str], level: int = 1
) -> str:
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


def _value_to_string2(
    value, indent: int | None, separators: tuple[str, str], level: int
) -> str:
    if isinstance(value, dict):
        return _dict_to_string(value, indent, separators, level=level)
    elif isinstance(value, list):
        return _list_to_string(value, indent, separators, level)
    return f"{value}"


def _value_to_string(value, float_fmt: str | None):
    if value is None:
        return _tostring_none()
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


def _dict_to_strings(d: dict, float_fmt: str | None) -> dict[str, str]:
    # convert everything to strings
    out = {}
    for key, value in d.items():
        assert isinstance(key, str)
        k = _tostring_str(key)
        out[k] = _value_to_string(value, float_fmt)
    return out


def _list_to_strings(lst: list, float_fmt: str | None) -> list:
    return [_value_to_string(value, float_fmt) for value in lst]


def _tostring_str(string: str) -> str:
    return f'"{string}"'


def _tostring_int(val: int) -> str:
    return str(val)


def _tostring_float(val: float, fmt: str | None) -> str:
    if fmt is None:
        return str(val)
    return f"{val:{fmt}}"


def _tostring_bool(val: bool) -> str:
    return "true" if val else "false"


def _tostring_none():
    return "null"
