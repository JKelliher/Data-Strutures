def getDigit(num, place): 
	x = num % 10**place
	y = x //10**(place-1)
	return(y)

def howmanydigits(num):
	count = 0
	z = num
	while z > 0:
		z = z/10
		count +=1
	return(count)

def mostdigits(li1):
	total = howmanydigits(li1[0])
	for num in li1:
		if howmanydigits(num) > total:
			total = howmanydigits(num)
	return(total)

def radixsort(li1):
	loops = mostdigits(li1)
	count = 1
	
	while count <= loops:
		digitBuckets = [[] for i in range(10)]
		
		for num in li1:
			x = (getDigit(num, count))
			digitBuckets[x].append(num)

		li1 = []
		for li in digitBuckets:
			for element in li:
				li1.append(element)

		count += 1

	return(li1)


x = [1,4,6,12,18,22,222,44444,101010, 7,0]
print(radixsort(x))