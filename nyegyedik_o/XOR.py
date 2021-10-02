#!/usr/bin/env python3


def main():
    str1 = "python"
    str2 = None

    print("python" + " is " + str(bool(str1)))
    print("None" + " is " + str(bool(str2)))
    if bool(str1) == bool(str2):
        print('Hamis, hogy az egyik érték igazként, míg a másik hamisra értékelődik')
    else:
        print('igaz, hogy az egyik igaz míg a másik hamis')

if __name__ == "__main__":
    main()
