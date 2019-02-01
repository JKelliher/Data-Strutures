from __future__ import division

def averagePair(l1,target):
	p1=0
	p2=len(l1)-1

	if len(l1) < 2:
		return(False)
	else:
		while p2 > p1:
			if float((l1[p1] + l1[p2])/2) > target:
				p2 -= 1

			elif float((l1[p1] + l1[p2])/2) < target:
				p1 += 1

			elif float((l1[p1] + l1[p2])/2) == target:
				return(True)

		return(False)

print(averagePair([1,2,3], 2.5))
print(averagePair([1,3,3,5,6,7,10,12,19], 8))
print(averagePair([-1,0,3,4,5,6],4.1))
print(averagePair([],4))