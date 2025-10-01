#!/usr/bin/env python3

def product(li):
    prod=1
    for i in li:
        prod*=i
    return prod 

def main():
    a=[1,2,3,4,5]
    print(product(a))

if __name__ == "__main__":
    main()
    