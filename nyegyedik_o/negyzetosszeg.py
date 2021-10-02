#!/usr/bin/env python3


def negyzetossz():
    result = 0
    for i in range(1,101):
        result += i**2
    return sum(range(1,101))**2 - result

def main():
    print(negyzetossz())


if __name__ == "__main__":
    main()
