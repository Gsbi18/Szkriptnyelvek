#!/usr/bin/env python3


def print_paper(smt:str) -> list:
    li=smt.split(",")
    newli=[]
    for i in li:
        if '-' in i:
            newi=i.split("-")
            for x in range(int(newi[0]),int(newi[1])+1):
                newli.append(x)
        else: 
            newli.append(int(i))
    return newli
def main():
    smt=input("Add meg a nyomtatandó oldalakat: ")
    print(print_paper(smt))


##################################################


if __name__ == "__main__":
    main()
    