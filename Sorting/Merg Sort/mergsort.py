def merge(ar1,ar2):
	ar3 = []
	ar1index = 0
	ar2index = 0

	while ar1index <= len(ar1)-1 or ar2index <= len(ar2)-1:

		if ar1index == len(ar1):
			ar3.append(ar2[ar2index])
			ar2index +=1

		elif ar2index == len(ar2):
			ar3.append(ar1[ar1index])
			ar1index +=1

		else:
			if ar1[ar1index] < ar2[ar2index]:
				ar3.append(ar1[ar1index])
				ar1index+=1

			else:
				ar3.append(ar2[ar2index])
				ar2index+=1
	return(ar3)


def merge_sort(ar1):
	if len(ar1) <=1:
		return(ar1)
	
	mid = len(ar1)//2

	print("ar1 left =", ar1[:mid])
	left = merge_sort(ar1[:mid])

	print("ar1 right=", ar1[mid:])
	right = merge_sort(ar1[mid:])
	
	print(merge(left,right))
	return(merge(left,right))

check=[10,9,8,7,6,6,5,4,3,50,6]
print(merge_sort(check))





















