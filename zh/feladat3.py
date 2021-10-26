#! /usr/bin/env python3 


def tri(n, k):
    return int((fact(n) / (fact(k) * fact(n - k))))


def fact(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res


def main():
    while True:
        sor = input('A sor indexe (kilépés: 0): ')
        index = int(sor)

        if index == 0:
            print('bye')
            break

        for i in range(0, index):
            print(tri(index - 1, i), end=' ')

        print('')


if __name__ == "__main__":
    main()