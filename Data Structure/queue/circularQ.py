class CircularQ:
	def __init__(self, size):
		self.front = -1
		self.rear = -1
		self.size = size
		self.CQ = [None for i in range(0,size)]

	def enque(self,data):
		if (self.rear+1)%self.size== self.front:
			print("Overflow")
			return
		elif self.front == -1 and self.rear == -1:
			self.front = self.rear = 0
			self.CQ[self.front] = data
		else:
			self.rear = (self.rear+ 1) % self.size
			self.CQ[self.rear] = data

	def deque(self):
		if self.front == -1:
			print("underflow")
			return
		elif self.front == self.rear:
			temp = self.CQ[self.rear]
			self.rear = self.front = -1
			# return temp
		else:
			temp = self.CQ[self.front]
			self.front = (self.front + 1) % self.size
			# return temp
		print(temp, 'is deleted')	

	def display(self):
		if self.front == -1:
			print("Queue is empty")
			return
		elif self.rear>=self.front:
			print()
			for i in range(self.front, self.rear+1):
				print(self.CQ[i], end=" ")
		else:
			print()
			for i in range(self.front, self.size):
				print(self.CQ[i], end=" ")
			for i in range(0, self.rear+1):
				print(self.CQ[i], end=" ")
	
	def Front(self):
		print(self.front)
		print(self.CQ[self.front])
	def Rear(self):
		print(self.rear)			
if __name__ == '__main__':
	cq = CircularQ(5)
	cq.enque(1)
	cq.enque(2)
	cq.enque(3)
	cq.enque(4)
	cq.enque(5)

	cq.display()

	cq.deque()
	cq.deque()
	cq.deque()
	cq.deque()



	cq.enque(6)
	
	cq.enque(20)
	cq.enque(30)
	cq.enque(30)
	cq.enque(30)



	cq.Front()

	cq.Rear()

	# cq.enque(40)
	# cq.enque(64)
	# cq.deque()
	# cq.enque(30)
	# cq.deque()
	# cq.enque(53)
	# cq.deque()
	cq.enque(54)

	# cq.deque()
	# cq.enque(57)
	# cq.deque()
	
	cq.display()
	
	# cq.enque(77)
	# cq.enque(88)
	# cq.enque(33)
	# cq.enque(11)

	# print(cq.CQ)
	# cq.display()



