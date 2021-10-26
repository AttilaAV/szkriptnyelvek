#! /usr/bin/env python3 
import math
 
def pitagorasz(a,b,c):
    if (pow(a,2) + pow(b,2)) == pow(c,2):
        return True
    return False


def main():
    feltetel = True

    a = 1
    b = 1

    while (a < 999 and feltetel):
        b = 1
        while (b < 999 and feltetel):
            c = 1000 - (a + b)
            if(pitagorasz(a,b,c)):
                feltetel = False;
            if feltetel:
                b = b + 1
        if feltetel:
            a = a + 1
    print (a, b, c)
    print (a*b*c)


if __name__ == "__main__":
    main()