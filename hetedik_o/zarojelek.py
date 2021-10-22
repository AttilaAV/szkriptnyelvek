#!/usr/bin/env python3

def test(kif):
    kerek = kif.count('(')-kif.count(')')
    szogletes = kif.count('[')-kif.count(']')
    kapcsos = kif.count('{')-kif.count('}')
    if kerek == szogletes == kapcsos == 0:
        return True
    else:
        return False



def main():
    print(test("((5+3)*2+1)"))
    print(test("{[(3+1)+2]+}"))
    print(test("(3+{1-1)}"))
    print(test("[1+1]+(2*2)-{3/3}"))
    print(test("(({[(((1)-2)+3)-3]/3}-3)"))


if __name__== '__main__':
    main()