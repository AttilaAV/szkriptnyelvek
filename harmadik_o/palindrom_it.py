#!/usr/bin/env python3


def palindrome(s):
	return s == s[::-1]


def main():
	s = input("Enter a string: ")
	ans = palindrome(s.lower())

	if ans:
		print("Palindrome")
	else:
		print("Not Palindrome")


if __name__ == "__main__":
	main()