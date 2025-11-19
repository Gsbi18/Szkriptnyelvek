#!/usr/bin/env python3

import random

def my_choice(li):
    rnd= random.randint(0,len(li)-1)
    return li[rnd]

def main():
    li=[1,2,3,4,5,6,7,8,9]
    print(my_choice(li))
##################################################


if __name__ == "__main__":
    main()
    