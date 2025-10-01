#!/usr/bin/env python3

def delwhitespace(s):
    s=s.split()
    s="".join(s)
    return s


def main():
    s="   206. 130.99. 82:\n8080   "
    print(delwhitespace(s))

if __name__ == "__main__":
    main()
    