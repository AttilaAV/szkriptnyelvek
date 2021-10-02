#!/usr/bin/env python3

def sum100():
    result = 0
    for i in range(1,101):
        result += sum_digits(i)
    return result


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def main():
    print(sum100())


if __name__ == "__main__":
    main()
