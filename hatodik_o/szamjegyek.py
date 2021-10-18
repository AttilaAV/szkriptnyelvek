#!/usr/bin/env python3

def sumofpower(base,power):
    szam = str(base**power)
    osszeg = 0
    for i in szam:
        osszeg += int(i)
    return osszeg



def main():
    print(sumofpower(2,1000))


if __name__== '__main__':
    main()

