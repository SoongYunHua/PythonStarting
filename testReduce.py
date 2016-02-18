#/usr/bin/python
from functools import reduce

def prod(L):
	def p(x, y):
		return x*y
	return reduce(p, L)

print(prod([1, 2, 3, 4]))