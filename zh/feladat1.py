#!/usr/bin/env python3


def number_of_houses(chars):
    rows = 0
    cols = 0
    cord = [(0,0)]
    for i in chars:
        if i == '^':
            rows += 1
        elif i == 'v':
            rows -= 1
        elif i == '>':
            cols += 1
        elif i == '<':
            cols -= 1
        tuple1 = (rows, cols)
        cord.append(tuple1)
    num_of_hous = len(set(cord))
    return num_of_hous


def main():
    f = open("input.txt","r")
    chrs = list(f.readline())
    print(number_of_houses(chrs))
    f.close()


if __name__ == "__main__":
    main()