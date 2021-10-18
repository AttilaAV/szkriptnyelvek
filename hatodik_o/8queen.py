#!/usr/bin/env python3

LISTA = [0,4,7,5,2,6,1,3]

def kiralynoproblema(lista):
    jatekter = [['.' for i in range(8)] for j in range(8)]

    ind = 0
    keret = "+ "+'- '*8+'+\n'
    tabla = keret
    for elem in lista:
        jatekter[7-elem][ind] = "Q"
        ind += 1
    for i in range(8):
        tabla += "| "
        for j in range(8):
            tabla += jatekter[i][j]
            tabla += ' '
        tabla += "|\n"
    tabla += keret
    return tabla


def main():
    print(kiralynoproblema(LISTA))
    

    
if __name__== '__main__':
    main()

