#!/usr/bin/env python3

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'


#words = ["ablak", "erkély", "kisvasút", "magas", "mély"]

def hangrend(word):
    mely=0
    magas=0
    for i in word:
        if i in MELY_MGHK:
            mely+=1
        elif i in MAGAS_MGHK:
            magas+=1
    
    if mely>0 and magas>0:
        return "Vegyes"
    if mely>0:
        return "Mély"
    if magas>0:
        return "Magas"
    if mely==0 and magas==0:
        return "Semelyik"


def main():
  print(hangrend("msdmsd"))


##################################################


if __name__ == "__main__":
    main()
    