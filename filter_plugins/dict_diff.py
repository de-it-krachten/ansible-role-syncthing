def dict_diff(a, b):
    """
    Recursively diff two dicts.
    Returns keys and values from `a` that differ from `b`.
    """
    result = {}
    for key in a.keys() | b.keys():
        if key not in b:
            result[key] = a[key]  # only in a
        elif key not in a:
            continue  # only in b, ignore (we're diffing a - b)
        else:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                nested = dict_diff(a[key], b[key])
                if nested:  # only include if differences exist
                    result[key] = nested
            elif a[key] != b[key]:
                result[key] = a[key]
    return result


class FilterModule(object):
    def filters(self):
        return {
            "dict_diff": dict_diff,
        }

