def selectionsort(ar1):
	count1 = 0

	while count1 < len(ar1) - 1:
		count2 = count1 + 1
		minv = ar1[count1]
		swap = False

		while count2 < len(ar1):
			if ar1[count2] < minv:
				minv = ar1[count2]
				index = count2
				swap = True
			count2 +=1

		if swap == True:
			temp = ar1[index]
			ar1[index] = ar1[count1]
			ar1[count1] = minv

		count1 +=1
		print("ar1 = ",ar1)
	return(ar1)


x = [16,1,15,7,8,4,6,7,8,10,4,13]
print(selectionsort(x))