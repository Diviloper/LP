def absValue(x):
    return x if x >= 0 else -x


def power(x, p):
    if p == 0:
        return 1
    else:
        y = power(x, p//2)
        return y*y if p % 2 == 0 else y*y*x


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


def slowFib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slowFib(n-1) + slowFib(n-2)


def quickFib(n: int) -> int:
    def aux(n: int) -> (int, int):
        if n == 0:
            return (0, 0)
        elif n == 1:
            return (0, 1)
        else:
            (n2, n1) = aux(n-1)
            return (n1, n1+n2)
    return aux(n)[1]
