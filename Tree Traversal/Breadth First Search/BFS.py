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

	def bfs(self,value):

		que = []
		visited = []
		found = False

		current = self.root
		que.append(current)

		while len(que) > 0:
			current = que[0]
			if current.left != None:
				que.append(current.left)
			if current.right != None:
				que.append(current.right)

			
			visited.append(que.pop(0).value)
		
		for num in visited:
			if num == value:
				found = True

		return(found)

	def dfs_pre_order(self,value):

		values = []
		found = False

		def helper(next_node):

			values.append(next_node.value)

			if next_node.left != None:
				helper(next_node.left)
			if next_node.right != None:
				helper(next_node.right)

		helper(self.root)
		print(values)

		for num in values:
			if num == value:
				found = True

		return(found)

	def dfs_post_order(self,value):

		values = []
		found = False

		def helper(next_node):

			if next_node.left != None:
				helper(next_node.left)
			if next_node.right != None:
				helper(next_node.right)

			values.append(next_node.value)

		helper(self.root)
		print(values)

		for num in values:
			if num == value:
				found = True

		return(found)

	def dfs_in_order(self,value):

		values = []
		found = False

		def helper(next_node):

			if next_node.left != None:
				helper(next_node.left)

			values.append(next_node.value)

			if next_node.right != None:
				helper(next_node.right)
				

		helper(self.root)
		print(values)

		for num in values:
			if num == value:
				found = True

		return(found)

x = node(10)
taco = BinarySearchTree()
taco.root = x
taco.root.right = node(15)
taco.root.right.right = node(18)
taco.root.left = node(8)
taco.insert(16)
taco.insert(9)
taco.insert(7)
taco.insert(1)
taco.insert(37)

print(taco.dfs_pre_order(37))
print(taco.dfs_post_order(37))
print(taco.dfs_in_order(37))



