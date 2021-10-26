#! /usr/bin/env python3 

import sys


def adatok(arg):
    f = open("data.csv", "r")
    sorok = f.readlines()
    for sor in sorok:
        nev = sor.split(';')[5]
        ssn = sor.split(';')[8]
        if ssn[0] == arg:
            print(nev +";"+ssn)
    f.close()


def main():
    if len(sys.argv) != 2:
        print("Hibás paraméterezés! Csak egy számjegyet kell megadni!")
    else:
        adatok(sys.argv[1])


if __name__ == "__main__":
    main()