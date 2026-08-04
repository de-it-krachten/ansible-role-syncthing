def recursive_sort(d):
    if isinstance(d, dict):
        return {k: recursive_sort(d[k]) for k in sorted(d)}
    elif isinstance(d, list):
        return [recursive_sort(x) for x in d]
    else:
        return d

class FilterModule(object):
    def filters(self):
        return {"recursive_sort": recursive_sort}

