def sumZero(list1):
	run = True
	index = 0
	sumz = 'undefined'

	while len(list1) > (1 + index):

		if abs(list1[index]) == list1[len(list1)-1]:
			sumz = True
			answer = [list1[index], abs(list1[index])]
			break

		elif abs(list1[index]) < list1[len(list1)-1]:
			list1.pop()

		elif abs(list1[index]) > list1[len(list1)-1]:
			index +=1	

	if sumz == True:
		return(answer)
	else:
		return(sumz)

print(sumZero([-5,-4,0,3]))
