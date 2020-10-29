class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

class DQ:
	def __init__(self):
		self.front = None
		self.rear = None

	def InsertBeg(self,data):
		temp = Node(data)

		if self.front == None:
			self.front = self.rear = temp
			return
		else:
			self.front.prev = temp
			temp.next = self.front
			self.front = temp

	def insertEnd(self,data):
		temp = Node(data)

		if self.front == None:
			self.front = self.rear = temp
			return
		else:
			temp.prev = self.rear
			self.rear.next = temp
			self.rear = temp

	def deleteBeg(self):
		if self.front == None:
			return
		self.front = self.front.next
		if self.front == None:
			self.rear = None
		else:
			self.front.prev = None

	def deleteEnd(self):
		if self.front == None:
			return
		self.rear = self.rear.prev
		if self.rear == None:
			self.front=None
		else:
			self.rear.next=None

	def visit(self):
		if self.front == None:
			print("Q is empty")
			return
		temp = self.front
		while(temp):
			print(temp.data, end=' ')
			temp=temp.next
if __name__ == '__main__':
	dq = DQ()
	dq.insertEnd(20)
	dq.InsertBeg(5)
	dq.insertEnd(10)
	dq.deleteBeg()
	dq.visit()

