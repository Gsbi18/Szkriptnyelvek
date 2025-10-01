#!/usr/bin/env python3

def listmult(list):
    base=1
    for i in list:
        base*=i
    return base

def main():
    list=[1,2,3,4,5]
    print("A lista elemeinek szorzata: ",listmult(list))

if __name__ == "__main__":
    main()
    