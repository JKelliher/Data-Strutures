def binarycontainssearch(ar1, value):

	while len(ar1) >= 1:
		pivot = len(ar1) // 2
		if ar1[pivot] < value:
			ar1 = ar1[pivot:]
		elif ar1[pivot] > value:
			ar1 = ar1[:pivot]
		elif ar1[pivot] == value:
			return(True)
		print(ar1)
	return(False)


def binarysearch(ar1, value):
	p1 = 0
	p2 = len(ar1)

	if ar1[0] == value:
		return(0)
	else:
		while p1 < p2-1:
			pivot = (p2 + p1) // 2
			if ar1[pivot] < value:
				p1 = pivot
			elif ar1[pivot] > value:
				p2 = pivot
			elif ar1[pivot] == value:
				return(pivot)

		return(False)


print(binarysearch([0,1,2,3,4,5,6,7,8,9],1))
print(binarysearch([0,1,2,3,4,5,6,7,8,9],2))
print(binarysearch([0,1,2,3,4,5,6,7,8,9],3))
print(binarysearch([0,1,2,3,4,5,6,7,8,9],4))
print(binarysearch([0,1,2,3,4,5,6,7,8,9],5))
print(binarysearch([0,1,2,3,4,5,6,7,8,9],6))
print(binarysearch([0,1,2,3,4,5,6,7,8,9],7))
print(binarysearch([0,1,2,3,4,5,6,7,8,9],8))

	

