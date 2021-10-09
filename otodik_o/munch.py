#!/usr/bin/env python3


def munch(num):
    res = 0
    if num == 0:
        return 0;
    for i in range(len(str(num))):
        r = num % 10
        res += r**r
        num = int(num/10)
    return res


def main():
    lista = []
    for i in range(440000000):
        print(i)
        if i == munch(i):
            lista.append(i)

    print(lista)

if __name__ == "__main__":
	main()