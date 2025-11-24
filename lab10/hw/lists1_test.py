import pytest
import lists1 as li1


def test_match():
    assert li1.match_ends(["aba", "xyz", "aa", "x", "bbb"]) == 3
    assert li1.match_ends(["", "x", "xy", "xyx", "xx"]) == 2
    assert li1.match_ends(["aaa", "be", "abc", "hello"]) == 1


def test_front_x():
    assert li1.front_x(["bbb", "ccc", "axx", "xzz", "xaa"]) == [
        "xaa",
        "xzz",
        "axx",
        "bbb",
        "ccc",
    ]
    assert li1.front_x(["ccc", "bbb", "aaa", "xcc", "xaa"]) == [
        "xaa",
        "xcc",
        "aaa",
        "bbb",
        "ccc",
    ]
    assert li1.front_x(["mix", "xyz", "apple", "xanadu", "aardvark"]) == [
        "xanadu",
        "xyz",
        "aardvark",
        "apple",
        "mix",
    ]
