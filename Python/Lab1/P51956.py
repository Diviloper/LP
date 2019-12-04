from functools import reduce


def myLength(l) -> int:
    i = 0
    for _ in l:
        i += 1
    return i


def myMaximum(l):
    return reduce(lambda acc, x: acc if acc > x else x, l)


def average(l):
    return sum(l) / len(l)


def buildPalindrome(l):
    return list(reversed(l)) + l


def remove(l1, l2):
    return list(filter(lambda x: x not in l2, l1))


def flatten(l):
    return [y for x in l for y in (flatten(x) if isinstance(x, list) else [x])]


def oddsNevens(l):
    return list(filter(lambda x: x % 2 == 1, l)), list(filter(lambda x: x % 2 == 0, l))


def primeDivisors(n):
    def isPrime(x: int) -> bool:
        if x < 2:
            return False
        elif x == 2:
            return True
        elif x % 2 == 0:
            return False
        for i in range(3, x, 2):
            if x % i == 0:
                return False
        return True

    return [x for x in range(2, n+1) if n % x == 0 and isPrime(x)]
