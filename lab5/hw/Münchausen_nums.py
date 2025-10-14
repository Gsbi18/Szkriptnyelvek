#!/usr/bin/env python3

def munchausen(n):
    sum=0
    for i in str(n):
        sum+=int(i)**int(i)

    if sum == n:
        return True
    else:
        return False
    
def main():
    print(0)
    i=0
    while True:
        if i>440_000_000:
            break
        else:
            if munchausen(i):
                print(i)
        i+=1
        

if __name__ == "__main__":
    main()
    