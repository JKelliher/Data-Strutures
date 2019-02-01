def minSubArrayLen(li, num):
	p1=0
	p2=1
	leng = len(li)
	passed = False

	if li[p1] >=num:
		return(1)

	else:
		rollsum = li[p1] + li[p2]
		while p2 < len(li):

			if rollsum < num and p2 == len(li)-1:
				break

			elif rollsum < num:
				p2 +=1
				rollsum = rollsum + li[p2]

			elif rollsum >= num and p1 < p2:
				if leng > (p2-p1):
					leng = (p2-p1)+1
				rollsum = rollsum - li[p1]
				p1+=1
				passed = True	

			elif rollsum >= num and p1 == p2:
				return(1)
		
		if rollsum < num and passed !=True:
			return(0)
		else:
			return(leng)

print(minSubArrayLen([2,3,1,2,4,3],7))
print(minSubArrayLen([2,1,6,5,4],9))
print(minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52))
print(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 39))
print(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 55))
print(minSubArrayLen([4, 3, 3, 8, 1, 2 ,3], 11))
print(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 95))


