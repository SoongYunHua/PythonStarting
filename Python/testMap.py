#/usr/bin/python

def firstUpper(x):
	return x.capitalize()

f = map(firstUpper, ["hello", "song", "yun", "hua"])

print(list(f))