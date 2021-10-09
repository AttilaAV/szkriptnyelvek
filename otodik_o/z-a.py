#!/usr/bin/env python3

import sys


def oda():
    """Az angol ABC betűít írja bele egy stringbe"""
    s = ""
    lst = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    for x in lst:
        s+=x
    return s

def vissza(s):
    """Megfordítja a kapott stringet"""
    return s[::-1]


def main():
    """A függvény futtatása függ a fáljnak a nevétől
    A mainben a függvénynevét nézzük meg."""

    if sys.argv[0][-6:]=="a-z.py":
        print(oda())
    elif sys.argv[0][-6:]=="z-a.py":
        print(vissza(oda()))


if __name__ == "__main__":
	main()