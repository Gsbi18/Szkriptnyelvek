import pytest
import string1


def test_donuts():
    assert string1.donuts(4) == "Fánkok száma: 4"
    assert string1.donuts(9) == "Fánkok száma: 9"
    assert string1.donuts(10) == "Fánkok száma: sok"
    assert string1.donuts(99) == "Fánkok száma: sok"


def test_both_ends():
    assert string1.both_ends("spring") == "spng"
    assert string1.both_ends("Hello") == "Helo"
    assert string1.both_ends("a") == ""
    assert string1.both_ends("xyz") == "xyyz"


def test_fix_start():
    assert string1.fix_start("babble") == "ba**le"
    assert string1.fix_start("aardvark") == "a*rdv*rk"
    assert string1.fix_start("google") == "goo*le"
    assert string1.fix_start("donut") == "donut"


def test_mix_up():
    assert string1.mix_up("mix", "pod") == "pox mid"
    assert string1.mix_up("dog", "dinner") == "dig donner"
    assert string1.mix_up("gnash", "sport") == "spash gnort"
    assert string1.mix_up("pezzy", "firm") == "fizzy perm"
