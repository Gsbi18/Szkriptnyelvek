#!/usr/bin/env python3
BIG = 1000000


def is_prime(n: int) -> bool:
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.

    Source: http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python
    """
    import random

    _mrpt_num_trials = 5  # number of bases to test

    #

    if n < 2:
        return False
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert 2**s * d == n - 1

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True  # n is definitely composite

    for _ in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True  # no base tested showed n as composite


def is_palindrome(s: int) -> bool:
    s = str(s)
    s = s.lower()
    return s == s[::-1]


def primepalindrome(n: int) -> int:
    for i in range(n, BIG):
        if is_prime(i) and is_palindrome(i):
            return i


def main():
    print(primepalindrome(4))
    print(primepalindrome(31))
    print(primepalindrome(130))
    print(primepalindrome(131))
    print(primepalindrome(1977))


##################################################


if __name__ == "__main__":
    main()
