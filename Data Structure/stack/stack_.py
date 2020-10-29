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





	# reversing stack with recursion
	def reverse(self):
		if self.isEmpty():
			return
		print(self.stack, self.top)
		temp = self.pop_2()
		self.reverse()

		self.insertAtBottom(temp)

	def insertAtBottom(self, item):
		if self.isEmpty():
			self.push(item)
			return

		temp = self.pop_2()
		self.insertAtBottom(item)

		self.push(temp)

	def sort(self):
		if self.isEmpty():
			return
		temp = self.pop_2()
		self.sort()
		self.insertSorting(temp)

	def insertSorting(self,item):
		if self.isEmpty() or self.topElement()<item:
			self.push(item)
			return
		temp = self.pop_2()
		self.insertSorting(item)
		self.push(temp)	

	def sortStack(self):
		tempStack = Stack(10)
		while self.isEmpty() == False:
			temp = self.pop_2()
			while(tempStack.isEmpty()==False and tempStack.topElement()>temp):
				self.push(tempStack.pop_2())
			tempStack.push(temp)
		tempStack.visit()
	#deleting middle 
	# def deleteMid(self,counter=0):
	# 	if self.isEmpty():
	# 		return
	# 	temp = self.pop_2()
	# 	counter = counter + 1
	# 	self.deleteMid(counter = counter )
	# 	half = counter//2
	# 	self.deleteM(temp, counter, half)

	# def deleteM(self, item, counter, half):
	# 	if self.isEmpty() or counter!=4:
	# 		self.push(item)
	# 		print("counter=",counter,"Half=",half)
	# 		return
	def deleteMid(self, count, n):
		if self.isEmpty():
			return
		temp = self.pop_2()
		count = count +1
		self.deleteMid(count,n)

		if count!=n:
			self.push(temp)

	# def reverseIndividualWords(words):
	# 	stack = Stack(len(words))
	# 	for i in words:
	# 		stack.push(i)
	# 		print(reverseString(stack))

	def reverseString(self):
		if self.isEmpty():
			return
		temp = self.pop_2()
		self.reverseString()
		self.insertAtBottom2(temp)

	def insertAtBottom2(self, item):
		if self.isEmpty():
			self.push(item)
			return
		temp = self.pop_2()
		self.insertAtBottom2(item)
		self.push(temp)		

    



if __name__ == '__main__':
	stack = Stack(10)
	stack.push(3)
	stack.push(1)
	stack.push(4)
	stack.push(7)
	stack.push(5)
	stack.push(6)
	stack.push(2)
	stack.visit()
	print("--------------------")
	# stack.reverse()
	stack.sort()
	# stack.sortStack()
	# stack.visit()
	n = stack.size()//2+1
	stack.deleteMid(0,n)
	stack.visit()

	str1 = "Birajit"
	strStack = Stack(len(str1))
	for i in str1:
		strStack.push(i)
	strStack.visit()
	strStack.reverseString()
	print("--------------------")
	strStack.visit()

		




