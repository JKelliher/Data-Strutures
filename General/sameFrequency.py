def samFrequency(num1, num2):
	dnum1 = {}
	dnum2 = {}
	snum1 = str(num1)
	snum2 = str(num2)

	for digit in snum1:
		if digit in dnum1:
			dnum1[digit]+=1
		else:
			dnum1[digit]=1

	for digit in snum2:
		if digit in dnum2:
			dnum2[digit]+=1
		else:
			dnum2[digit]=1

	if dnum1 == dnum2:
		return(True)

	else:
		return(False)


print(samFrequency(182, 281))
print(samFrequency(34, 14))
print(samFrequency(3589578, 5879385))
print(samFrequency(22, 222))