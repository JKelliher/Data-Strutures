class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def push(self, val):
		x = Node(val)

		if self.head == None:
			self.head = x
			self.tail = x

		else:
			self.tail.next = x
			self.tail = x

		self.length +=1
		return(self)
	
	def pop(self):
		if self.length == 0:
			return(False)

		else:
			tail = self.tail.val
			count = 0
			current = self.head

			while count < self.length - 2:
				current = current.next
				count +=1

			current.next = None
			self.length -=1

			if self.length ==0:
				self.tail = None
				self.head = None

			return(tail)
	
	def traverse(self):
		current = self.head
		while current != None:
			print(current.val)
			current = current.next

	def shift(self):
		if self.length != 0:
			current = self.head
			self.head = current.next
			
			if self.head == None:
				self.tail = None
			
			self.length -= 1

			return(current.val)

		else:
			return(False)

	def unshift(self, val):
		x = Node(val)
		
		if self.length == 0:
			self.tail = x
			
		else:
			x.next = self.head

		self.head = x
		self.length+=1
		return(self)

	def get(self, nodep):
		if nodep >= self.length:
			return(False)

		elif nodep < 0:
			return(False)

		else:
			count = 0
			current = self.head

			while count < nodep:
				current = current.next
				count+=1
			return(current)

	def set(self, val, nodep):
		x = self.get(nodep)
		if x == False:
			print("Node not found")
			return(False)
		else:
			x.val = val

	def insert(self, val, nodep):
		if nodep < 0 or nodep > self.length:
			return(False)

		elif nodep == 0:
			self.unshift(val)

		elif nodep == self.length:
			self.push(val)

		else:
			y = Node(val)
			x = self.get(int(nodep) - 1)
			y.next = x.next
			x.next = y
			self.length +=1
		return(True)

	def remove(self, nodep):

		if nodep < 0 or nodep >= self.length:
			return(False)

		elif nodep == 0:
			self.shift()
			return(True)

		elif nodep == int(self.length-1):
			self.pop()
			return(True)

		else: 
			x = self.get(int(nodep) - 1)
			y = self.get(nodep)
			x.next = y.next
			self.length -=1
			return(True)

	def reverse(self):
		if self.length == 0:
			return(self)
		else:
			self.tail = self.head

			current = self.head
			y = current.next
			current.next = None

			while y != None:
				x = y.next
				y.next= current
				current = y
				y = x
			self.head = current
			return(self)