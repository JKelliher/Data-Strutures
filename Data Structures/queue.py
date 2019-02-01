class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def enque(self, val):
		x = Node(val)

		if self.head == None:
			self.head = x
			self.tail = x
		else:
			self.tail.next = x
			self.tail = x

		self.length +=1
		return(self)

	def deque(self):
		if self.length != 0:
			current = self.head
			self.head = current.next
			
			if self.head == None:
				self.tail = None
			
			self.length -= 1

			return(current.val)

		else:
			return(False)

food = Queue()
food.enque('taco')
food.enque('burrito')
food.enque('nacho')
print("")

print(food.deque())
print(food.deque())
print(food.deque())