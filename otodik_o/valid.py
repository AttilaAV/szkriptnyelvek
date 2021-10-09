#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
	"""A függvény egy olyan (akár üres) sztringgel tér vissza
	 mely a "text"-ből (első paraméter) csak azokat a karaktereket tartalmazza
	  melyek szerepelnek a "chars"-ban. """
	  
	s = ""
	for x in text:
		if x in chars:
			s += x
	return s


def main():
	print(valid("Barking!"))
	print(valid("KL754", "0123456789"))
	print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz")) 


if __name__ == "__main__":
	main()