def sigma(x: int, n: int) -> int:
    d = 1
    s = 0
    while d <= n:
        if n % d == 0:
            s += d ** x
        d += 1
    return s


def totient(n: int) -> float:
    prod = 1
    p = 2
    while p <= n:
        if n % p == 0:
            p_ = p // 2
            prime = True
            while p_ > 1:
                if p % p_ == 0:
                    prime = False
                p_ -= 1
            if prime:
                prod *= 1 - 1 / p
        p += 1
    return n * prod
        