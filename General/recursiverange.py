def recursiverange(num):
	if num == 0:
		return(0)
	return(num + recursiverange(num-1))

print(recursiverange(6))