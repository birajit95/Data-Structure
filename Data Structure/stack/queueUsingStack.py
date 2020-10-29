class Stack:
	def __init__(self, size):
		self.top = -1
		self.maxSize = size
		self.stack = []

	def visit(self):
		if self.top < 0:
			print("Stack is empty")
			return
		for i in range(0,self.top+1):
			print(self.stack[i])

	def push(self, data):
		if self.top == self.maxSize-1:
			print("Overflow")
			return
		self.top +=1
		self.stack.append(data)

	def pop_2(self):
		if self.top < 0:
			return "Underflow Condition"
		self.data = self.stack[self.top]
		self.stack.pop()
		self.top = self.top-1
		return self.data

	def isEmpty(self):
		return self.top<0

	def topElement(self):
		if self.top < 0 :
			print('Stack is empty')
			return
		return self.stack[self.top]

	def size(self):
		return self.top+1

class Queue:
	def __init__(self, size):
		self.s1 = Stack(size)
		self.s2 = Stack(size)
		self.max = size

	def enque(self,data):
		if self.s1.size==self.max:
			print("Overflow")
		else:
			self.s1.push(data)

	def deque(self):
		if self.s1.isEmpty():
			return
		self.s2.push(self.s1.pop_2())
		self.deque()
		self.s2.pop_2()
		while(not self.s2.isEmpty()):
			self.s1.push(self.s2.pop_2())
	def qVisit(self):
		self.s1.visit()	

if __name__ == '__main__':
	q = Queue(7)
	q.enque(1)
	q.enque(2)
	q.enque(3)
	q.enque(4)
	q.enque(5)
	q.qVisit()
	q.deque()
	print("----------------------")
	q.qVisit()
