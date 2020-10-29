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

def checkPriority(op,stack):
	opertaor = {'+':1,'-':1,'*':2,'/':2,'^':3}
	top = stack.topElement()
	if opertaor.get(op)>opertaor.get(top):
		return True
	else:
		return False
def isOperand(ch):
	return ch.isalpha()

def infixToPrefix(exp, stack, output):
	for i in exp:
		if isOperand(i):
			output.append(i)
		elif i == '(':
			stack.push(i)
		elif i==')':
			while(stack.topElement()!='(' and not stack.isEmpty()):
				op4 = stack.pop_2()
				output.append(op4)
			stack.pop_2()	
		else:
			if stack.isEmpty():
				stack.push(i)
			else:
				if stack.topElement()=='(':
					stack.push(i)
				if checkPriority(i, stack):
					stack.push(i)
				else:
					opp = stack.pop_2()
					output.append(opp)
					stack.push(i)
	while(not stack.isEmpty()):
		op3 = stack.pop_2()
		output.append(op3)
	return output				

def prefixToInfix(exp, stack):
	for i in exp[::-1]:
		if isOperand(i):
			stack.push(i)
		else:
			a = stack.pop_2()
			b = stack.pop_2()
			c = '('+a+i+b+')'
			stack.push(c)
	stack.visit()		

def postFixToInfix(exp,stack):
	for i in exp:
		if isOperand(i):
			stack.push(i)
		else:
			b = stack.pop_2()
			a = stack.pop_2()
			c = '('+a+i+b+')'
			stack.push(c)
	stack.visit()		

def prefixToPostfix(exp,stack):
	for i in exp[::-1]:
		if isOperand(i):
			stack.push(i)
		else:
			a = stack.pop_2()
			b = stack.pop_2()
			c = a+b+i
			stack.push(c)
	stack.visit()

def postFixToPrefix(exp, stack):
	for i in exp:
		if isOperand(i):
			stack.push(i)
		else:
			b = stack.pop_2()
			a = stack.pop_2()
			c = i+a+b
			stack.push(c)
	stack.visit()			
if __name__ == '__main__':
	# output = []
	# exp = "A+B*C/(D+E)-F"
	# stack = Stack(len(exp))
	# output = (infixToPrefix(exp, stack, output))
	# st = ''
	# for i in output:
	# 	st = st+i
	# print(st)


	# exp = '*-A/BC-/AKL'
	# stack=Stack(10)
	# prefixToInfix(exp, stack)

	# exp = 'abc++'
	# stack=Stack(5)
	# postFixToInfix(exp, stack)
	
	# exp = '*-A/BC-/AKL'
	# stack=Stack(5)
	# prefixToPostfix(exp, stack)

	exp = 'ABC/-AK/L-*'
	stack=Stack(5)
	postFixToPrefix(exp,stack)
