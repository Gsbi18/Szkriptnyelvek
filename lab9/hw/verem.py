#!/usr/bin/env python3


class Verem:
    def __init__(self):
        self.lista = []

    def ures(self):
        if len(self.lista) == 0:
            return True
        else:
            return False

    def betesz(self, value):
        self.lista.append(value)

    def kivesz(self):
        if len(self.lista) == 0:
            return None
        return self.lista.pop()

    def meret(self):
        return len(self.lista)

    def __str__(self):
        kiir = str(self.lista)
        kiir = kiir.replace("]", "")
        return kiir


def main():
    v = Verem()  # üres verem létrehozása

    print(v)  # [
    print(v.ures())  # True

    v.betesz(1)
    v.betesz(4)
    v.betesz(5)

    print(v)  # [1 4 5
    print(v.meret())  # 3
    print(v.ures())  # False

    x = v.kivesz()
    print(x)  # 5
    print(v)  # [1 4

    v.kivesz()
    v.kivesz()  # most már üres

    x = v.kivesz()
    print(x)  # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


##############################################################################

if __name__ == "__main__":
    main()
