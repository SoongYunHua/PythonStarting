#!/user/bin/python

'''
def triangle():
	L = [1]
	while True:
		yield L
		i = len(L) - 1
		while i:
			L[i] = L[i] + L[i-1]
			i = i - 1
		L.append(1)
'''

def triangle():
	L = [1]
	while True:
		yield L
		L = [1] + [x + y for x, y in zip(L[0:], L[1:])] + [1]

n = 0
for t in triangle():
	print(t)
	n = n + 1
	if n == 10:
		break

