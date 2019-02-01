class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Stack:
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def pop(self):
		if self.size != 0:
			current = self.first
			self.first = current.next
			
			if self.first == None:
				self.last = None
			
			self.size -= 1

			return(current.val)

		else:
			return(False)

	def push(self, val):
		x = Node(val)
		
		if self.size == 0:
			self.last = x
			
		else:
			x.next = self.first

		self.first = x
		self.size+=1
		return(self.size) 

taco = Stack()
taco.push('carne asada')
taco.push('carnitas')
taco.push('al pastor')

print(taco.pop())
print(taco.pop())
print(taco.pop())