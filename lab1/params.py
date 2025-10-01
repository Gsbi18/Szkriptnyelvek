#!/usr/bin/env python3

import sys


def Hello(name):
    if  name == "Batman" or name=="Robin":
        print("Denevérveszély")
    else:
        print("Hello "+ name+ "!")


def main():
    name=sys.argv[1]
    Hello(name)


if __name__ == "__main__":
    main()