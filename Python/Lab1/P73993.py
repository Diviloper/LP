from functools import reduce


def evens_product(l):
    return reduce(lambda acc, x: acc * x, list(filter(lambda x: x % 2 == 0, l)), 1)


def reverse(l):
    return reduce(lambda acc, x: [x] + acc, l, [])


def zip_with(f, l1, l2):
    return list(map(lambda x: f(*x), zip(l1, l2)))


def count_if(f, l):
    return len(list(filter(lambda x: f(x), l)))
