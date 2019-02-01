def bubblesort(ar1):
	n = 0
	temp = 0
	
	while n < len(ar1):
		m = 0
		swapcount = 0
		while m < len(ar1)-1-n:
			if ar1[m] > ar1[m+1]:
				temp = ar1[m]
				ar1[m] = ar1[m+1]
				ar1[m+1]=temp
				swapcount += 1
			m+=1
		if swapcount > 0:
			n+=1
		else:
			break
	return(ar1)



artest = [10,9,8,7,6,5,4,3,2,1,0,1000000]
artest2 = [0,1,2,3,4,5,6,7]
print(bubblesort(artest))