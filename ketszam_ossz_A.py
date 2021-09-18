#!/usr/bin/env python3

import sys


def sum(a, b):
    return a + b;


def main():

    if len(sys.argv) < 3:
        print("bad input")
    else:
        sys.argv[1] = int(sys.argv[1])
        sys.argv[2] = int(sys.argv[2])
        print(sum(sys.argv[1], sys.argv[2]))






if __name__ == "__main__":
	main()