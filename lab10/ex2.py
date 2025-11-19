#!/usr/bin/env python3
from pygyak import is_prime,hello


def main():
    sum=0
    for i in range(200):
        if is_prime(i):
            sum+=i
    print(sum)
    print(hello())
##################################################


if __name__ == "__main__":
    main()
    