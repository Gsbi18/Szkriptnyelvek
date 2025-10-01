#!/usr/bin/env python3

def is_palindrom3(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrom3(s[1:-1])

def is_palindrom2(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    print(is_palindrom3("orog"))
if __name__ == "__main__":
    main()
    