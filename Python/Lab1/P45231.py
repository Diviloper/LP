def fibs():
    yield 0
    prev = 0
    curr = 1
    while True:
        yield curr
        prev, curr = curr, curr + prev


def roots(x):
    prev = x
    yield prev
    while True:
        curr = 0.5 * (prev + x/prev)
        yield curr
        prev = curr


def primes():
    n = 2
    while True:
        if (isPrime(n)):
            yield n
        n += 1


def hammings():
    n = 1
    while True:
        if isHammings(n):
            yield n
        n += 1


def isHammings(n):
    for i in range (7, n+1, 2):
        if n%i == 0 and isPrime(i):
            return False
    return True


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
