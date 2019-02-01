def maxSubarraySum(li, size):
	if len(li) < size:
		return('null')
	else:
		p1 = 0
		p2 = 0
		tempsum = 0

		while p2 < size:
			tempsum += li[p2]
			p2+=1

		
		maxs = tempsum
		
		while p2 < len(li):
			tempsum = tempsum + li[p2] - li[p1]
			if maxs < tempsum:
				maxs = tempsum
			p1+=1
			p2+=1
		return(maxs)

print(maxSubarraySum([100,200,300,400],2))
print(maxSubarraySum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
print(maxSubarraySum([-3,4,0,-2,6,-1],2))
print(maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2))
print(maxSubarraySum([2,3],3))
