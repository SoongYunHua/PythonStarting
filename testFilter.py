#!/usr/bin/python
def notEmpty(s):
	print(s)
	return s and s.strip()

print(list(filter(notEmpty, [' 10', '5', '', None,])))

string = ' 10'
print(string and string.strip())