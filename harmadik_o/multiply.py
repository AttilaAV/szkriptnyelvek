#!/usr/bin/env python3


def multiply(list):
	result = 1
	for e in list:
		result *= e
	return result



def main():
	list = [1,2,3,4,5,6]
	print(multiply(list))


if __name__ == "__main__":
	main()