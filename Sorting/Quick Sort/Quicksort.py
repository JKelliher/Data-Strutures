def pivotf(ar1, start=0, end= -10):
	pivot = ar1[start]
	swapindex = start
	count = start + 1

	if end == -10:
		end = len(ar1)

	while count < end:
		if pivot > ar1[count]:

			swapindex +=1
			temp = ar1[swapindex]
			ar1[swapindex] = ar1[count]
			ar1[count] = temp

		count+=1

	temp = ar1[swapindex]
	ar1[swapindex] = ar1[start]
	ar1[start] = temp

	return(swapindex)

def quicksort(ar1, left=0, right=-10):
	if right == -10:
		right = len(ar1)

	if left < right:
		pivotindex = pivotf(ar1, left, right)
		# left
		quicksort(ar1,left, pivotindex)
		# right
		quicksort(ar1, pivotindex+1, right)
		

	return(ar1)

print(quicksort([4,7,3,2,3,8,5,6,2]))
print(quicksort([1,2,1]))
print(quicksort([2,1,2]))
print(quicksort([10,20,30,41,1,3,2,4,5,6,7,10]))
print(quicksort([2,4,6,5,3]))
print(quicksort([2,1]))
print(quicksort([2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]))
print(quicksort([9,8,7,6,5,4,3,3,2,1]))


