Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def findmax(l):
	leng = len(l)
	if len(l) == 1:
		return l
	elif leng(l-1) > leng(l-2):
		del leng(l-2)
		
SyntaxError: can't delete function call
>>> def findmax(l):
	leng = len(l)
	if len(l) == 1:
		return l
	elif l[leng-1] > l[leng-2]:
		del l[leng-2]
	elif l[leng-1] < l[leng-2]:
		del l[leng-1]
	findmax(l)

	
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
>>> 
