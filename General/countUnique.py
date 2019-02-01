def countUniqueValues(ar1):
	
	if len(ar1) == 0:
		return(0)

	elif len(ar1) == 1:
		return(1)

	else:
		p1 = 0
		p2 = 1
		total = 1

		while p2 <= len(ar1) -1:
			if ar1[p1] == ar1[p2]:
				p2+=1
			else:
				total +=1
				p1 = p2
				p2+=1

		return(total)


print(countUniqueValues([1,2]))