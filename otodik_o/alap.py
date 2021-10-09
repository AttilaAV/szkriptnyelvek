#!/usr/bin/env python3


def hello(name, repeat=1, postfix=""):
	for i in range(repeat):
		print(name + postfix)


def main():
	hello("laci")
	print("-" * 28)
	hello("Laci", repeat=2, postfix="!")


if __name__ == "__main__":
	main()