def anagramChecker(str1, str2):

	if len(str1) != len(str2):
		return(False)
	
	else:
		st1dic = {}
		for letter in str1:
			if letter in st1dic:
				st1dic[letter] +=1
			else:
				st1dic[letter]=1

		for letter in str2:
			if letter in st1dic:
				if st1dic[letter] >=1:
					st1dic[letter] -=1
				else:
					return(False)
					break
			else:
				return(False)
				break
		return(True)

print(anagramChecker('tacolovinwhore', 'tacowhorelovin'))