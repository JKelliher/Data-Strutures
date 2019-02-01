def insertionsort(ar1):
	count = 1

	while count < len(ar1):
		if ar1[count] < ar1[count-1]:

			count2 = count-1
			temp = ar1[count]

			while temp < ar1[count2] and count2 >= 0:

				ar1[count2+1] = ar1[count2]
				count2 -= 1
			ar1[count2+1] = temp

		count +=1
		print(ar1)

	return(ar1)

x = [10,9,8,7,8,9,4,3,11,12]
print(insertionsort(x))