def isSubsequence(st1, st2):
	p1 = 0
	p2 = 0
	
	while p1 < len(st1) and p2 < len(st2):
		if st1[p1] == st2[p2]:
			p1 +=1

		else:
			p2 +=1

	if p2 == len(st2):
		return(False)
	else:
		return(True)

print(isSubsequence('abc', 'acb'))