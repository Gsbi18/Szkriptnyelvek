#!/usr/bin/env python3

import sys


def main():
#v1    
    if len(sys.argv)<3:
        print("Hiba adj meg pontosan két számot!!!")
        return 0
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    print(f"A(z) {a} és a {b} számoknak az összege: {a+b}")
#v2
    #a2=input("Első szám: ")
    #b2=input("Második szám: ")
    #print(f"A(z) {a2} és a {b2} számoknak az összege: {int(a2)+int(b2)}")

    
    
if __name__ == "__main__":
    main()
    