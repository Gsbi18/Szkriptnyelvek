#!/usr/bin/env python3


def hello(name, repeat=1, postfix=''):
    for i in range(repeat):
        print(name+postfix)

def main():
    #hello("Gabi")
    #hello("Gabi" ,repeat=3)
    hello("Gabi" ,repeat=3,postfix='!')


##################################################


if __name__ == "__main__":
    main()
    