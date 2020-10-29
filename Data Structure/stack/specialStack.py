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

	def push(self, data, obj):
		if self.top == self.maxSize-1:
			print("Overflow")
			return
		self.top +=1
		self.stack.append(data)
		if obj.isEmpty():
			obj.top+=1
			obj.stack.append(data)
		else:
			if obj.topElement()>data:
				obj.top +=1
				obj.stack.append(data)
			else:
				obj.stack.append(obj.topElement())
				obj.top +=1

	def min(self, obj):
		return obj.topElement()

	def pop_2(self,obj):
		if self.top < 0:
			return "Underflow Condition"
		self.data = self.stack[self.top]
		self.stack.pop()
		self.top = self.top-1
		obj.stack.pop()
		obj.top-=1
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

if __name__ == '__main__':
	s1 = Stack(10)
	s2 = Stack(10)
	s1.push(10, s2)
	s1.push(20, s2)
	s1.push(5, s2)
	s1.push(30, s2)
	s1.push(50, s2)
	s1.push(2, s2)
	s1.pop_2(s2)
    	
	s1.visit()
	print("======================")
	print(s1.min(s2))


