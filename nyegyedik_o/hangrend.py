#!/usr/bin/env python3


def hangrend(word):
    MELY = 'aáoóuú'
    MAGAS = 'eéiíöőüű'
    mely_count = 0;
    magas_count = 0;

    for i in word:
        if i in MELY:
            mely_count += 1
        if i in MAGAS:
            magas_count += 1

    if mely_count != 0 and magas_count == 0:
        print(word + " mély")
    if mely_count == 0 and magas_count != 0 :
        print(word + " magas")
    if mely_count != 0 and magas_count != 0:
        print(word + " vegyes")
    if mely_count == 0 and magas_count == 0:
        print(word + " semmi")

def main():


    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfff"]
    for word in words:
        hangrend(word)


if __name__ == "__main__":
    main()
