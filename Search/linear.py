def linearSearch(ar1, value):
	count = 0
	for x in ar1:
		if x == value:
			return(count)
		count+=1
	return(-1)


print(linearSearch([1,2,3,4],6))
