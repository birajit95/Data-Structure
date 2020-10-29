class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
	def __init__(self):
		self.front = self.rear = None
		self.total = 0

	def visit(self):
		if self.front==None and self.rear == None:
			print("Queue is Empty")
			return
		temp = self.front
		while temp!=self.rear.next:
			print(temp.data)
			temp = temp.next	

	def enque(self, data):
		temp = Node(data)
		
		if self.front==None and self.rear == None:
			self.front=self.rear = temp
			self.total +=1
			return
		self.rear.next = temp
		self.rear = self.rear.next
		self.total +=1

	def deque(self):
		if self.front == None and self.rear == None:
			print('Underflow')
		elif self.front == self.rear:
			temp = self.front
			temp = None
			self.rear = self.front = None
			self.total = 0
		else:
			temp = self.front
			temp = None
			self.front= self.front.next
			self.total -=1
	def Front(self):
		return self.front.data

	def Rear(self):
		return self.rear.data

	def size(self):
		return self.total				

if __name__ == '__main__':
	q = Queue()
	q.enque(10)
	q.enque(20)
	q.enque(30)
	q.enque(40)
	q.enque(50)
	q.enque(60)
	q.enque(70)
	q.enque(80)
	q.enque(90)
	q.enque(100)
	q.visit()
	print("---------------------------")
	print(q.Rear())
	print(q.Front())
	print("---------------------------")
	print(q.size())
	q.deque()
	q.deque()
	q.deque()
	q.deque()
	q.deque()
	q.deque()
	q.deque()
	q.deque()
	q.deque()
	q.deque()
	q.deque()
	q.enque(200)

	print("---------------------------")
	q.visit()


