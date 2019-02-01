class node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__ (self):
		self.root = None

	def insert(self, value):

		x = node(value)

		if self.root == None:
			self.root = x

		current = self.root
		direction = None

		while current != None:

			if x.value > current.value:
				previous = current
				direction = "right"
				current = current.right	

			elif x.value < current.value:
				previous = current
				direction = "left"
				current = current.left

		current = x
		if direction == "right":
			previous.right = x
		if direction == "left":
			previous.left = x
		return(self)

	def search(self,value):

		current = self.root
		found = False

		while current != None:
			if current.value == value:
				found = True
				break

			elif value > current.value:
				current = current.right

			elif value < current.value:
				current = current.left

		return(found)

	def find(self, value):

		current = self.root
		found = False

		while current != None:
			if current.value == value:
				found = True
				break

			elif value > current.value:
				current = current.right

			elif value < current.value:
				current = current.left

		return(current)


x = node(10)
taco = BinarySearchTree()
taco.root = x
taco.root.right = node(15)
taco.root.right.right = node(18)
taco.root.left = node(8)

taco.insert(16)

print(taco.root.right.right.left.value)






