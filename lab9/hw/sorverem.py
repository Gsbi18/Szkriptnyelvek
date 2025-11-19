#!/usr/bin/env python3

class Verem(list):
    def ures(self):
        """Igazat ad vissza, ha a verem üres."""
        return len(self) == 0

    def betesz(self, value):
        """Elem betétele a verembe."""
        self.append(value)

    def meret(self):
        """A verem méretének lekérdezése."""
        return len(self)

    def kivesz(self):
        """Elem kivétele a veremből (LIFO). Ha üres, None-t ad vissza."""
        if not self.ures():
            return self.pop()
        else:
            return None

    def __str__(self):
        """Szép megjelenítés: [1 4 5"""
        return "[" + " ".join(map(str, self))  # nincs záró ]

def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük, hogy üres veremből vettünk ki)

if __name__ == "__main__":
    main()
