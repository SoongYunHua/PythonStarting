#!/usr/bin/python

def odd_iter():
	n = 1
	while True:
		n = n+2
		yield n

print(list(odd_iter()))