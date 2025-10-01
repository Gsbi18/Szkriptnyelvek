#!/usr/bin/env python3

MSG="""
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

def caesar(msg, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message = ""
    for i in msg:
        if i.islower():
            position = alphabet.find(i)
            new_position = (position + key) % len(alphabet)
            new_character = alphabet[new_position]
            new_message += new_character
        elif i.isupper():
            position = alphabet2.find(i)
            new_position = (position + key) % len(alphabet2)
            new_character = alphabet2[new_position]
            new_message += new_character
        elif i == "\t":
            new_message += "\t"
        elif i == "\n":
            new_message += "\n"
        elif i == " ":
            new_message += " "
    return new_message


def main():
    key = 2
    print("Megfejtett üzenet: \n", caesar(MSG, key))


if __name__ == "__main__":
    main()
    