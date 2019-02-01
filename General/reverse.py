def reverse(str):
	x=list(str)
	y=[]

	def helper(lis):
		if len(lis) == 0:
			return()
		y.append(lis.pop())
		return(helper(lis))
	helper(x)
	return(''.join(y))



print(reverse('taco'))
