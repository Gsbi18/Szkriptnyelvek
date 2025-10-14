#!/usr/bin/env python3

def main():
#1. feladat
    be1=['auto', 'villamos', 'metro'] #→ ['AUTO!', 'VILLAMOS!', 'METRO!']
    print([n.upper()+"!" for n in be1])
    
#2. feladat
    be2=['aladar', 'bela', 'cecil'] #→ ['Aladar', 'Bela', 'Cecil']
    print([n.capitalize() for n in be2])
    
#3. feladat
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], azaz inicializáljunk egy 10-elemű listát csupa 0-val.
    print([ 0 for n in range(0,11)])
    
#4. feladat
    be4=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #→ [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print([ n*2 for n in be4])
    
#5. feladat
    be5=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] #→ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (az első listában sztringek vannak)
    print([int(n)  for n in be5])
    
#6. feladat
    be6="1234567" #→ [1, 2, 3, 4, 5, 6, 7], vagyis van számunk sztring formátumban, s egy listába be akarjuk tenni a számjegyeit (számokként)
    print([int(n) for n in be6])
    
#7. feladat
    be7='The quick brown fox jumps over the lazy dog' #→ [3, 5, 5, 3, 5, 4, 3, 4, 3], vagyis állapítsuk meg az egyes szavak hosszát
    print([len(n) for n in be7.split(" ")])
    
#8. feladat
    be8="python is an awesome language" #→ ['p', 'i', 'a', 'a', 'l'], vagyis egy sztring szavainak a kezdőbetűit gyűjtsük össze egy listában
    print([n[0] for n in be8.split(" ") ])
    
#9. feladat
    be9='The quick brown fox jumps over the lazy dog' #→ [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)], vagyis a listában tuple-öket helyezzünk el a következő szerkezettel: (szó, szóhossz).
    print([(n, len(n)) for n in be9.split(" ")])
    
#10. feladat
#[0, 2, 4, 6, 8], vagyis állítsuk elő egy listában a 10-nél kisebb páros számokat
    print([n for n in range(1,10) if n%2==0])
    
#11. feladat
#Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak a párosakat hagyjuk meg ([0, 4, 16, 36, 64, 100, 144, 196, 256, 324]).
    print([n**2 for n in range(0,20) if n**2%2==0])
    
#12. feladat
#Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak azokat hagyjuk meg, melyeknek az utolsó számjegye "4" ([4, 64, 144, 324]).
    print([n**2 for n in range(0,20) if str(n**2)[-1]=='4'])
    
#13. feladat
#Gyűjtsük össze az angol ábécé nagybetűit egy listában (használjuk a chr függvényt), majd fűzzük össze az elemeket egyetlen sztringgé: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    print(''.join([chr(c) for c in range(ord('A'), ord('Z') + 1)]))

#14. feladat
    be14=[' apple ', ' banana ', ' kiwi'] #→ ['apple', 'banana', 'kiwi'], vagyis a listában lévő szavak elejéről és végéről távolítsuk el a whitespace karaktereket
    print([n.strip() for n in be14])
    
#15. feladat
    be15=[1, 0, 1, 1, 0, 1, 0, 0] #→ "10110100", vagyis a listában lévő számjegyeket fűzzük össze egy sztringgé
    print(''.join([str(szam) for szam in be15]))
    
##################################################


if __name__ == "__main__":
    main()
    