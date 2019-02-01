class Max_heap:

	def __init__(self):
		self.values = []

	def insert(self,value):
		self.values.append(value)

		index = len(self.values)-1
		parent_ind = self.parent_index(index)

		while self.values[index] > self.values[parent_ind]:
			temp = self.values[parent_ind]
			self.values[parent_ind] = self.values[index]
			self.values[index] = temp
			index = parent_ind
			parent_ind = self.parent_index(index)
			if parent_ind <0:
				break
		return(self)

	def extract_max(self):
		


	def parent_index(self,index):
		import math
		parent = math.floor((index-1)/2)
		return(int(parent))

	def left_child_index(self,index):
		left_child = 2*index+1
		return(left_child)

	def right_child_index(self,index):
		right_child = 2*index+2
		return(right_child)

	

x = Max_heap()
x.insert(10)
x.insert(11)
x.insert(12)
x.insert(14)
x.insert(15)
x.insert(16)
x.insert(17)
x.insert(1)

print(x.values)
