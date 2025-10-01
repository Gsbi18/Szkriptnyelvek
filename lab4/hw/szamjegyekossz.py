#!/usr/bin/env python3


def main():
    szamok = ""
    counter=0
    for i in range(1,101):
        szamok+=str(i)
        
    for i in szamok:
        counter+=int(i)
    print(counter)
    
    
##################################################


if __name__ == "__main__":
    main()
    