#!/usr/bin/env python3

def is_palindrome(s:int) ->bool:
    s=str(s)
    s = s.lower()
    return s == s[::-1]

def to_binary(n:int) ->str:
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    return bits or "0"

def main():
    sum=0
    for i in range(1000000):
        if is_palindrome(i) and is_palindrome(to_binary(i)):
            sum+=i
    print(sum)
##################################################


if __name__ == "__main__":
    main()
    