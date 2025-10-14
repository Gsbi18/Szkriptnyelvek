#!/usr/bin/env python3
import sys
import string
import os

nev = os.path.basename(sys.argv[0])

abc = string.ascii_lowercase

if "z-a" in nev:
    print(abc[::-1])
else:
    print(abc)
