#!/usr/bin/env python3


def reverse(s):
    return int(s[::-1])


def main():
    n = input("Enter a INT number: ")
    print(reverse(n))


if __name__ == "__main__":
	main()