#!/usr/bin/env python3


def main():
    li = ['Alfa', 'Beta','Gamma']
    cnt=0
    for i in li:
        print(i,cnt)
        cnt+=1
    
    for index,e in enumerate(li,start=1):
        print(index,e)

if __name__ == "__main__":
    main()
    