#!/usr/bin/env python3


def palindrome(s):
	if len(s) < 2:
		return True
	if s[0] != s[-1]:
		return False
	return palindrome(s[1:-1])


def main():
	s = input("Enter a string: ")
	ans = palindrome(s.lower())

	if ans:
		print("Palindrome")
	else:
		print("Not Palindrome")


if __name__ == "__main__":
	main()