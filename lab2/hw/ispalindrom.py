#!/usr/bin/env python3


def ispalindrom(s):
    if s == s[::-1]:
        return True
    else:
        return False
     
    
def main():
    s="görög"
    if ispalindrom(s):
        print(f"A {s} szó palindróm.")
    else:
        print(f"A {s} szó nem palindróm.")

if __name__ == "__main__":
    main()