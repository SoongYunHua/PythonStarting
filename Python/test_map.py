#!/usr/bin/python

def fun(x):
	return x*x

r = map(fun, (1, 2, 3, 4, 5))

print(list(r))