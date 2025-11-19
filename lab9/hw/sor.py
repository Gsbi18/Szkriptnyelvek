#!/usr/bin/env python3


class Sor:
    def __init__(self):
        self.lista = []

    def beszuras(self, value):
        self.lista.append(value)

    def torles(self):
        copy = self.lista
        kivett = list(reversed(copy)).pop()
        self.lista.remove(kivett)
        return list(reversed(copy)).pop()

    def isempty(self):
        if len(self.lista) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.lista)

    def __str__(self):
        return str(self.lista)


def main():
    s = Sor()
    s.beszuras(8)
    s.beszuras(7)
    s.beszuras(6)
    s.beszuras(2)
    s.beszuras(8)
    print(s)
    s.torles()
    print(s)


##############################################################################

if __name__ == "__main__":
    main()
