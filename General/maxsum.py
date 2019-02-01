def maxsum(ar1, num):
	if num > len(ar1):
		return('undefined')
	else:
		j=0
		rollsum = 0
		while j < num:
			rollsum += ar1[j]
			j+=1

		i = 0
		maxs = rollsum

		while j < len(ar1):
			rollsum = rollsum + ar1[j] - ar1[i]
			if rollsum > maxs:
				maxs=rollsum
			i+=1
			j+=1
		return(maxs)

print(maxsum([1,1,1,1,2,3,1,1,1], 4))