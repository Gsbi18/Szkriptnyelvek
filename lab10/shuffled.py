#!/usr/bin/env python3

import random

def shuffled(li):
    new=li.copy()
    random.shuffle(new)
    return new

def main():
    li=[1,2,3,4,5,6,7,8,9]
    n=shuffled(li)[-1]
    
    print(n)
    print(li)
##################################################


if __name__ == "__main__":
    main()
    