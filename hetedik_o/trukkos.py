#!/usr/bin/env python3

import binascii

def bin_to_dec(binaris):
    szorozhato = binaris[::-1]
    szam = 0
    for i in range(8):
        szam += int(szorozhato[i])*(2**(i))
    return szam


def main():
    with open ("ORC_of_trukkos", 'r') as file:
        szoveg = file.read().replace('\n', ' ')
        szamok = szoveg.strip().split()
        for szam in szamok:
            print(chr(int(bin_to_dec(szam))), end='')
    print("\n")
    
            

    


if __name__== '__main__':
    main()