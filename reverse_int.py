#!/usr/bin/env python3


def reverse(n):
	rev = 0

	while(n!=0):
		r = int(n%10)
		rev = rev*10 + r
		n = int(n/10)

	return rev


def main():
	print(reverse(789))



if __name__ == "__main__":
	main()