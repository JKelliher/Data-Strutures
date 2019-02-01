def areThereDuplicates(*argv):
	check = {}
	for arg in argv:
		if str(arg) in check:
			return(True)
			break
		else:
			check[str(arg)]=1
	return(False)


print(areThereDuplicates(1,2,3))
print(areThereDuplicates(1,2,2))
print(areThereDuplicates('a', 'b', 'c', 'a'))