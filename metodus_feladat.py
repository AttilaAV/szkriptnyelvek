#!/usr/bin/env python3

#sztring metódus feladat
#A program kér egy szót és visszaadja ennek a nagybetűs változatát.


def upper(s):
    print("Here is the uppercase version: " + s.upper())


def main():
    word = input("Please enter a word: ")
    upper(word)


if __name__ == "__main__":
    main()