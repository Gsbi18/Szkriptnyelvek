#!/usr/bin/env python3


class MyQueue:
    def __init__(self):
        self.verem1 = []
        self.verem2 = []

    def append(self, value):
        self.verem1.append(value)

    def popleft(self):
        for index in range(len(self.verem1)):
            self.verem2.append(self.verem1.pop())

        popolas_eredmenye = self.verem2.pop()

        for index in range(len(self.verem2)):
            self.verem1.append(self.verem2.pop())

        return popolas_eredmenye

    def is_empty(self):
        if len(self.verem1) == 0 and len(self.verem2) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.verem1)

    def __str__(self):
        return str(self.verem1).replace("[", "")


def main():
    sor = MyQueue()
    print(sor.is_empty())
    sor.append(5)
    sor.append(1)
    sor.append(3)
    sor.append(6)

    print(sor.is_empty())

    print(sor)

    print(sor.size())

    x = sor.popleft()
    print(x)
    print(sor.size())
    print(sor)


##############################################################################

if __name__ == "__main__":
    main()
