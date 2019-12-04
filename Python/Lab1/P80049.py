from functools import reduce


def count_unique(l):
    return len(set(l))


def remove_duplicates(l):
    return list(set(l))


def flatten(l):
    return reduce(lambda acc, x: acc + x, l, [])

def flatten_rec(l):
    return reduce(lambda acc, x: acc + (flatten_rec(x) if isinstance(x, list) else [x]), l, [])