#!/usr/bin/env python3


def match_ends(words):
    counter = 0
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            counter += 1

    return counter


def front_x(words):
    words2 = []
    words3 = []
    for i in words:
        if i[0] == "x":
            words2.append(i)
        else:
            words3.append(i)
    words3.sort()
    words2.sort()
    words2.extend(words3)
    return words2


def main():
    pass


#############################################################################

if __name__ == "__main__":
    main()
