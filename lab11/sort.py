#!/usr/bin/env python3


def main():
    # word = ["ccc", "aa", "b", "dddd"]
    # print(sorted(word,key=len))
    # word = ["CCC", "AA", "b", "dddd"]
    # print(sorted(word, key=str.lower))
    # def my_func(s):
    #   return s[-1]

    # word = ["aa", "xc", "zb", "yd"]
    # print(sorted(word, key=my_func))

    data = [
        (1, "Albany", "NY", 162692),
        (121, "Wyoming", "NY", 8722),
        (3, "Allegany", "NY", 11986),
        (123, "Yates", "NY", 5094),
    ]

    def tuplelast(tuple):
        return tuple[-1]

    # print(sorted(data, key=tuplelast))
    # print(sorted(data, key=lambda t: t[-1]))

    users = ["10:User1", "80:User2", "100:User3", "00:User4", "75:User4", "45:User5"]

    def id(s):
        tmp = s.split(":")
        return int(tmp[0])

    # print(sorted(users, reverse=True, key=id))
    # print(sorted(users, reverse=True, key=lambda s: int(s.split(":")[0])))
    matrix = [[2, 6], [1, 3], [5, 4]]

    def func(m):
        return m[1]

    # print(sorted(matrix, key=func))
    # print(sorted(matrix, key=lambda t: t[1]))


##################################################


if __name__ == "__main__":
    main()
