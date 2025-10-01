#!/usr/bin/env python3

def szamfordit(szam):
    szoszam=str(szam)
    szoszam= szoszam[::-1]
    return int(szoszam)

def main():
    print(szamfordit(1998), type(szamfordit(1998)))

if __name__ == "__main__":
    main()
    