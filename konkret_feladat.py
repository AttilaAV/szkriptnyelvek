#!/usr/bin/env python3

#sztring metódus feladat
#A program kér egy szót és visszaadja ennek a nagybetűs változatát.


def name(s):
    print("Hello " + s.strip() + "!")


def main():
    word = input("Please enter your name: ")
    name(word)


if __name__ == "__main__":
    main()