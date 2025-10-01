#!/usr/bin/env python3

def osszegnegyzert(n):
    osszegnegyzert=0
    for i in  n-1:
        osszegnegyzert=i+i+1
    return pow(osszegnegyzert,2)

def main():
    osszegnegyzert(10)

if __name__ == "__main__":
    main()