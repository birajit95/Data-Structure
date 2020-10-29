class Queue:
	def __init__(self, size):
		self.front = -1
		self.rear = -1
		self.max = size
		self.queue = []
		self.size = 0

	def visit(self):
		if(self.front == -1 and self.rear == -1):
			print("Queue is empty")
		else:
			i = self.front
			while(i<=self.rear):
				print(self.queue[i])
				i+=1



	def enque(self, data):
		if self.rear == self.max-1:
			print("Overflow")
		elif(self.front == -1 and self.rear == -1):
			self.front = self.rear = 0
			self.queue.append(data)
			self.size+=1
		else:
			self.rear += 1
			self.queue.append(data)
			self.size+=1

	def deque(self):
		if(self.front == -1 and self.rear == -1):
			print("Underflow")
			return
		elif(self.rear == self.front):
			data = self.queue[self.front]
			self.rear = self.front = -1
			self.size = 0
		else:
			data = self.queue[self.front]
			self.front+=1
			self.size -=1
		return data

	def isEmpty(self):
		return (self.rear == -1	and self.front==-1)
	def Size(self):
		return self.size	
	def Front(self):
		return self.queue[self.front]

	def Rear(self):
		return self.queue[self.rear]

class Stack:
	def __init__(self, size):
		self.q1 = Queue(size)
		self.q2 = Queue(size)
		self.max = size
		self.total = 0

	def push(self, data):
		self.q1.enque(data)
		self.total+=1

	def pop(self):
		if self.q1.isEmpty():
			return
		while self.q1.Size()>1:
			self.q2.enque(self.q1.deque())
		self.q1.deque()
		self.q1,self.q2 = self.q2,self.q1
	
	def travel(self):
		self.q1.visit()
		print("size", self.q1.Size())

if __name__ == '__main__':
	s = Stack(10)
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(5)
	s.push(6)
	s.push(7)
	s.travel()
	s.pop()
	s.pop()
	s.pop()
	s.pop()
	
	print('=============')
	s.travel()




		