#!/usr/bin/python
# _*_ coding: utf-8 _*_
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(key):
	return key[0]

def by_score(key):
	return key[1]

print(L)
print(sorted(L, key=by_name))
print(sorted(L, key=by_score))