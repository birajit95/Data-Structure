class Node:
	def __init__(self, data, priority):
		self.data = data
		self.priority = priority
		self.next = None

class PriorityQ:
	def __init__(self):
		self.front = None
		self.rear = None

	def enque(self, data, priority):
		temp = Node(data, priority)

		if self.front == None and self.rear == None:
			self.front = self.rear = temp
			return
		elif self.front.priority<temp.priority:
			temp.next = self.front
			self.front = temp
		else:
			start = self.front
			while(start.next!=None and start.next.priority>=temp.priority):
				start = start.next

			temp.next = start.next
			start.next = temp

	def deque(self):
		if self.front == None and self.rear ==None:
			print("Underflow")
			return
		temp = self.front.data
		self.front = self.front.next
		return temp

	def visit(self):
		if self.front == None:
			print("Q is empty")
			return
		temp = self.front
		while(temp!=None):
			print(f"{temp.data}==>{temp.priority}")
			temp = temp.next

if __name__ == '__main__':
	p = PriorityQ()

	p.enque("A",2)
	p.enque("B",4)
	p.enque("C",1)
	p.enque("X",6)
	# p.enque("Y",3)
	# p.enque("Z",5)
	p.enque("L",6)
	p.enque("T",3)
	p.enque("D",5)


	p.visit()
