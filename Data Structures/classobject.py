class Student:
	def __init__(self, firstname, lastname, grade):
		self.firstname = firstname
		self.lastname = lastname
		self.grade = grade
		self.tardies = 0
		self.scores = []

	def fullname(self):
		return("Student's Full name is " + self.firstname + " " + self.lastname)

	def nextgrade(self):
		currentgrade = self.grade
		nextgrade = str(currentgrade + 1)
		return('The next grade for ' + self.firstname + " " + self.lastname + " is " + nextgrade)

	def marklate(self):
		self.tardies +=1
		tard = str(self.tardies)
		if tard == "1":
			return(self.firstname + " " + self.lastname + " has been late " + tard + " time.")
		else:
			return(self.firstname + " " + self.lastname + " has been late " + tard + " times")

	def addscore(self, score):
		self.scores.append(score)

	def averagescore(self):
		sum = 0
		count = 0
		for score in self.scores:
			sum = sum + score
			count +=1
		return(sum / count)

	@classmethod
	def enrollstudent(Student):
		return("Students have been enrolled!")


firststudent = Student("John", "Doe", 12)
secondstudent = Student("jane", "doe", 8)


print(firststudent.fullname())
print(firststudent.nextgrade())
print(firststudent.marklate())
print(firststudent.marklate())

secondstudent.addscore(80)
secondstudent.addscore(70)
print(secondstudent.scores)
print(secondstudent.averagescore())

print(Student.enrollstudent())