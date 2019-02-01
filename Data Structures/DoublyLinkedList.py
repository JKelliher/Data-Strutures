class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.previous = None

class DoublyLinkedList:
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
			x.previous = self.tail
			self.tail = x

		self.length +=1
		return(self)

	def traverse(self):
		current = self.head
		while current != None:
			print(current.val)
			current = current.next

	def traversereverse(self):
		current = self.tail
		while current != None:
			print(current.val)
			current = current.previous

	def pop(self):
		if self.length == 0:
			return(False)

		else:
			x = self.tail
			self.tail = self.tail.previous
			self.tail.next = None
			self.length -= 1
			x.previos = None
		return(x.val)

	def shift(self):
		if self.length != 0:
			current = self.head
			self.head = current.next
			self.head.previous = None
			
			if self.head == None:
				self.tail = None
			
			self.length -= 1
			current.next=None
			return(current.val)

		else:
			return(False)

	def unshift(self, val):
		x = Node(val)
		
		if self.length == 0:
			self.tail = x
			
		else:
			x.next = self.head
			self.head.previous = x

		self.head = x
		self.length+=1
		return(self) 

	def get(self, nodep):
		if nodep >= self.length:
			return(False)

		elif nodep < 0:
			return(False)
		
		elif nodep <= (self.length / 2)-1:
			count = 0
			current = self.head

			while count < nodep:
				current = current.next
				count+=1
			return(current)

		else:
			count = self.length -1
			current = self.tail

			while count > nodep:
				current = current.previous
				count -=1
			return(current)

	def set(self, val, nodep):
		x = self.get(nodep)
		if x == False:
			print("Node not found")
			return(False)
		else:
			x.val = val
			return(True)

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
			z = self.get(int(nodep))

			y.next = x.next
			y.previous = x

			x.next = y
			z.previous = y

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
			z = self.get(int(nodep) + 1)

			x.next = y.next
			z.previous = y.previous
			self.length -=1

			y.next = None
			y.previous = None
			return(True)

	def reverse(self):
		if self.length == 0:
			return(self)

		current = self.head

		while current!= None:
			x = current.previous
			y = current.next

			current.previous = y
			current.next = x

			current = y

		x = self.tail
		y = self.head

		self.tail = y
		self.head = x

		return(self)