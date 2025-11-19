#!/usr/bin/env python3


def main():
    f = open("input.txt", "r")

    content = f.read().splitlines()

    result = 0
    index = 0
    for sor in content:
        temp = sor.split()
        for elem in temp:
            # Át alakítom az szöveget számmá
            elem = int(elem)
            # Itt vannak kilistázva a számok
            if index == 0:
                # Az első elemet megadom a min-nek és a max-nak
                min = elem
                max = elem
            if min > elem:
                min = elem

            if max < elem:
                max = elem
            index += 1
        reszleg = max - min
        result += reszleg
        min = 0
        max = 0
        index = 0

    print(result)
    f.close()


##############################################################################

if __name__ == "__main__":
    main()
