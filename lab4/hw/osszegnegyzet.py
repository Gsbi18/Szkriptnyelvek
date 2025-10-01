#!/usr/bin/env python3

def negyzetosszeg(num):
    counter=0
    for i in range(1, num+1):
        counter+=pow(i,2)
    return counter

def osszegnegyzet(num):
    counter=0
    for i in range(1, num+1):
        counter+=i
    return pow(counter,2)

def main():
    print(osszegnegyzet(100)-negyzetosszeg(100))


##################################################


if __name__ == "__main__":
    main()
    