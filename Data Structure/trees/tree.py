import pdb
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

	def isEmpty(self):
		if(self.front==-1 and self.rear==-1):
			return True
		return False	

	def Front(self):
		return self.queue[self.front]
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



class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# class Tree:
# 	def __init__(self):
# 		self.root = None

def insert(root, node):
		if root == None:
			root = node
			return root
		else:	
		    if root.data>=node.data:
		    	if root.left==None:
		    		root.left=node
		    	else:
		    		insert(root.left, node)
		    else:
		    	if root.right == None:
		    		root.right=node
		    	else:
		    		insert(root.right, node)
		    return root

def findMin(root):
	if root == None:
		return False
	if root.left == None:
		return root.data
	else:
		while(root.left!=None):
			root=root.left
		return root.data

def findMinRecursively(root):
	print(root.data)
	if root.left==None:
		return root.data
	findMinRecursively(root.left)

def findMax(root):
	if root==None:
		return False
	if root.right == None:
		return root.data
	while(root.right!=None):
		root = root.right
	return root.data				

def height(root):
	if root==None:
		return -1
	h_left = height(root.left)
	h_right = height(root.right)
	return max(h_left, h_right)+1

def search(root, key):
	if root == None:
		print(False)
		return False
	print(root.data, key)

	if root.data == key:
		print(True)
		return True
	if key<=root.data:
		search(root.left, key)
	else:
		search(root.right, key)



def leveOrderTraverse(root):
		q = Queue(20)
		q.enque(root)
		while(q.isEmpty()==False):
			cur = q.deque()
			print(cur.data,end=" ")
			if cur.left!=None:
				q.enque(cur.left)
			if cur.right!=None:
				q.enque(cur.right)

def PreOrder(root):
	s = Stack(20)
	s.push(root)

	while s.isEmpty() == False:
		cur = s.topElement()
		s.pop_2()
		if cur.right:
			s.push(cur.right)
		if cur.left:
			s.push(cur.left)
		print(cur.data,end = " ")
	print("")

def PreOredRecursively(root):
	if root==None:
		return
	print(root.data,end=" ")
	PreOredRecursively(root.left)
	PreOredRecursively(root.right)

def InOrder(root):
	s = Stack(20)
	cur = root
	while True:
		if cur!= None:
			s.push(cur)
			cur = cur.left
		elif(s.isEmpty() == False):
			cur = s.topElement()
			s.pop_2()
			print(cur.data, end=" ")
			cur = cur.right
		else:
			break	
def peek(s):
	if(len(s)>0):
		return s[-1]
	return False	
def PostOrder(root):
	cur = root
	# s = Stack(10)
	s =[]
	while True:
		while cur:
			if cur.right:
				s.append(cur.right)
			s.append(cur)
			cur = cur.left

		if(len(s)!=0):
			cur = s.pop()
			if cur.right == peek(s):
				s.pop()
				s.append(cur)
				cur = cur.right
			else:
				print(cur.data,end=" ")
				cur = None
		else:
			break	
def findMaxNode(root):
	if root==None:
		return False
	if root.right.right == None:
		return root
	while(root.right.right!=None):
		root = root.right
	return root
  
def deleteNode(root, key):
	if root == None:
		return
	if root.data<key:
		deleteNode(root.right, key)
	elif root.data>key:
		deleteNode(root.left, key)
	else:
		if root.left == None and root.left == None:
			root = None
		elif root.left == None:
			root = root.right
		elif root.right == None:
			root = root.left
# 
		else:
			parent = deleteNode(root.left)
			max = parent.right
			if max.left:
				parent.right = max.left
			max.left = root.left
			max.right = root.right
		# return root

		




if __name__ == '__main__':
			t = None
			t=insert(t, Node(10))
			t=insert(t, Node(4))
			t=insert(t, Node(12))
			t=insert(t, Node(3))
			t=insert(t, Node(15))
			t=insert(t, Node(18))
			t=insert(t, Node(1))
			t=insert(t, Node(5))
			leveOrderTraverse(t)
			print('======')
			print('min:',findMin(t))
			# print('findMinRecursively:',findMinRecursively(t))
			print("max:",findMax(t))
			print("height:",height(t))
			x = search(t, 18)
			# print(x)

			# print("PreOrder====")
			# PreOrder(t)
			# print("PreOredRecursively====")
            
			# PreOredRecursively(t)
			# print("Inorder")
			# InOrder(t)
			# print('PostOrder')
			# PostOrder(t)
			print("\ndelete")
			# pdb.set_trace()
			deleteNode(t,18)
			# pdb.set_trace()

			leveOrderTraverse(t)




