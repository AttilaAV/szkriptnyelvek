#!/usr/bin/env python3

def karakterek(szo):
    szo = szo.lower().strip().replace(" ", "")
    klista = [c for c in szo]
    klista = sorted(klista)
    return klista


def benne_van_e(szo1, szo2):
    lista1 = karakterek(szo1)
    lista2 = karakterek(szo2)
    if (lista1 == lista2) == True:
        return ("A két szó egymás anagrammája")
    else:
        return("A két szó nem egymás anagrammája")



def main():
    print("listen = silent \t", benne_van_e("listen", "silent"))
    print("A gentleman = Elegant man\t", benne_van_e("A gentleman", "Elegant man"))
    print("Clint Eastwood = Old west action\t", benne_van_e("Clint Eastwood", "Old west action"))
    print("dormitory = dirty room\t", benne_van_e("dormitory", "dirty room"))
    print("Pista = Tapsifüles \t", benne_van_e("Pista", "Tapsifüles"))



if __name__== '__main__':
    main()

