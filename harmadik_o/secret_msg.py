#!/usr/bin/env python3

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def decode(s):
    result = ""
    for c in s:
        if c.islower():
            if c >= 'a' and c <= 'z':
                result += chr(((ord(c) + 2) - ord('a')) % 26 + ord('a'))
            else:
                result += c
        else:
            if c >= 'A' and c <= 'Z':
                result += chr(((ord(c) + 2) - ord('A')) % 26 + ord('A'))
        else:
                result += c
    return result

def main():
    print(decode(TEXT))


if __name__ == "__main__":
	main()