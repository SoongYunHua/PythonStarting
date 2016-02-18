#!/usr/bin/python
from functools import reduce

def str2float(s):
	def prod(x, y):
		return x*10 + y

	def fn(x, y):
		return x/10 + y

	def char2num(pos):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[pos]

	L = s.split('.')
	return reduce(prod, map(char2num, L[0])) + reduce(fn, map(char2num, L[1][::-1]))/10

print(str2float('123.455'))