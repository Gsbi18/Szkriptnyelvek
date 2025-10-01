#!/usr/bin/env python3

import sys

MAX = 10


def hello(name,color,what):
    #print("{0}, {1} az {2}!".format(name,color,what))
    #print("{}, {} az {}!".format(name,color,what))
    #print("{nev}, {szin} az {obj}!".format(nev=name,szin=color,obj=what))
    print(f"{name.capitalize()}, {color} az {what}!")
    
def main():
    hello("géza", "kék", "ég")
    print("-"*20)
    hello("peti", "pios", "autó")

if __name__ == "__main__":
    main()