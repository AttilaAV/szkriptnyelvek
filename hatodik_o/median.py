#!/usr/bin/env python3

def median(nums):
    lista = []
    for i in nums:
        lista.append(i)
    lista = sorted(lista)
    print(lista)
    hossz = len(lista)
    if hossz % 2 == 1:
        median = lista[int(hossz/2)]
    else:
        median = (lista[int(hossz/2)]+lista[int((hossz/2))-1])/2
    return median




def main():
    print(median([1, 2, 3, 4, 5]) == 3)
    print(median([3, 1, 2, 5, 3]) == 3)
    print(median([1, 300, 2, 200, 1]) == 2)
    print(median([3, 6, 20, 99, 10, 15]) == 12.5)
    print(median([3, 6, 10, 99, 10, 15]) == 12.5)
    


if __name__== '__main__':
    main()

