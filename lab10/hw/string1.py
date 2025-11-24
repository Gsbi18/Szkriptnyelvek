#!/usr/bin/env python3

def donuts(count:int) -> str:
    if count < 10:
        return f"Fánkok száma: {count}"
    else:
        return f"Fánkok száma: sok"
    

def both_ends(s:str)->str:
    if  len(s)<2:
        return ""
    else:
        return (s[:2]+s[-2:])


def fix_start(s:str)->str:
    char=s[0]
    s=s[1:].replace(char,"*")
    return char+s


def mix_up(a:str, b:str)->str:
    tempa = a[:2]
    tempb = b[:2]
    tempao=a[2:]
    tempbo=b[2:]
    return tempb+tempao+" "+tempa+tempbo

def main():
   pass
#############################################################################

if __name__ == '__main__':
    main()