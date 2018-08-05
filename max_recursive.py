>>> listA = [1, 3, 4, 123, 542, 56, 78, 990, 23]
>>> findmax(listA)
>>> def findmax(l):
	leng = len(l)
	if len(l) == 1:
		return l
	elif l[leng-1] > l[leng-2]:
		del l[leng-2]
	elif l[leng-1] < l[leng-2]:
		del l[leng-1]
	return findmax(l)

>>> findmax(listA)
[990]
