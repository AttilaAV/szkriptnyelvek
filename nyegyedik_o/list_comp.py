#!/usr/bin/env python3


def feladat1():
    lst = ['auto', 'villamos', 'metro']
    return [x.upper() + "!" for x in lst]

def feladat2():
    lst = ['aladar', 'bela', 'cecil']
    return [x.capitalize() for x in lst]

def feladat3():
    return [x*0 for x in range(10)]


def feladat4():
    lst = [1,2,3,4,5,6,7,8,9,10]
    return [x*2 for x in lst]


def feladat5():
    lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    return[int(x) for x in lst]


def feladat6():
    s = '1234567'
    return [int(x) for x in s]

def feladat7():
    s = 'The quick brown fox jumps over the lazy dog'
    return [len(x) for x in s.split()]

def feladat8():
    s = "python is an awsome language"

    return [x[0] for x in s.split()]


def feladat9():
    s = 'The quick brown fox jumps over the lazy dog'
    return tuple([(x, len(x)) for x in s.split()])


def feladat10():
    return [x for x in range(10) if x%2==0]


def feladat11():
    return[x**2 for x in range(20) if x%2==0]


#def feladat12():
    #return[x**2 for x in range(20) if x[]]

def main():
    print(feladat1())
    print(feladat2())
    print(feladat3())
    print(feladat4())
    print(feladat5())
    print(feladat6())
    print(feladat7())
    print(feladat8())
    print(feladat9())
    print(feladat10())
    print(feladat11())

if __name__ == "__main__":
    main()
