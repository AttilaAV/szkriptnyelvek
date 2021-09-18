#!/usr/bin/env python3


def palindrom(s):
    return s ==s[::-1]


def main():
    word = input("Enter a word: ")
    word = word.lower()
    ans = palindrom(word)

    if ans:
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
	main()