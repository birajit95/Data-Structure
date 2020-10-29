class Queue:
	def __init__(self, size):
		self.front = -1
		self.rear = -1
		self.max = size
		self.queue = []

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
			self.front = 0
			self.rear = 0
			self.queue.append(data)
		else:
			self.rear += 1
			self.queue.append(data)

	def deque(self):
		if(self.front == -1 and self.rear == -1):
			print("Underflow")
			return
		elif(self.rear == self.front):
			data = self.queue[self.front]
			self.rear = -1
			self.front = -1
			self.queue.clear()
		else:
			data = self.queue[self.front]
			self.front+=1
		return data	

	def Front(self):
		return self.queue[self.front]

	def Rear(self):
		return self.queue[self.rear]

if __name__ == '__main__':
		q = Queue(7)
		q.enque(10)
		q.enque(20)		
		q.enque(30)		
		q.enque(40)		
		q.enque(50)
		q.visit()
		q.deque()
		q.deque()
		q.deque()
		q.deque()
		q.deque()
		q.deque()
		q.deque()
		q.enque(1)
		q.enque(2)
		q.enque(3)
		q.enque(4)
		q.enque(5)


		print("________________________")		
		q.visit()
		print("________________________")
		# print(q.Front())
		# print(q.Rear())

