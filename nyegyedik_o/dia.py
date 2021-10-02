#!/usr/bin/env python3

def diamond(szam):
    if (szam % 2) != 1:
        print("Kérlek, páratlan számot adj meg!")
    else:
        gyemantfel = int(szam/2)+1
        sorcsillag = 1
        for i in range(gyemantfel):
            csillag =sorcsillag*"*"
            sorcsillag += 2
            print(csillag.center(szam))
        sorcsillag -= 2
        for i in range(gyemantfel-1):
            sorcsillag -= 2
            csillag =sorcsillag*"*"
            print(csillag.center(szam))
    return ''



def main():
    hanyas = int(input("Mekkora legyen a gyémántod? "))
    print(diamond(hanyas))


if __name__== '__main__':
    main()