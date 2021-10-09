#!/usr/bin/env python3


def thousand():
    
    """Felsorolja és összeadja az 1000nél kisebb inteket

    Amennyiben azok a három vagy az ötnek a töbszörösei"""


    return sum([x for x in range(1000) if x%3==0 or x%5==0])


def main():
    print(thousand())


if __name__ == "__main__":
	main()