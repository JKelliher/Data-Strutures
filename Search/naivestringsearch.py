def naivestringsearch(st1,st2):
	st1l = list(st1)
	st2l = list(st2)
	n = 0
	
	countmatch = 0

	while n < len(st1l):
		if st1l[n] == st2l[0]:
			z = n
			m = 0
			count = 0

			while m < len(st2l) and z <= len(st1l)-1:
				if st1l[z] != st2l[m]:
					break	
				z += 1
				m += 1
				count += 1
			
			if count == len(st2l):
				countmatch +=1
		n+=1

	return(countmatch)
print(naivestringsearch('tacotacostaco', 'tacos'))