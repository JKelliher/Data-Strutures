def ispalindrome(strin):
	x=list(strin)
	y=[]

	def helper(lis):
		if len(lis) == 0:
			return()
		y.append(lis.pop())
		return(helper(lis))
	helper(x)
	Y = ''.join(y)

	if Y == strin:
		return(True)
	else:
		return(False)

print(ispalindrome('taat'))