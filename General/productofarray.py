def productofarray(ar1):
	if len(ar1) == 0:
		return(1)
	return(ar1.pop()*productofarray(ar1))

x = [1,2,3,4,5]

print(productofarray(x))
