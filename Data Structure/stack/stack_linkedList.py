class StackNode:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.top = 0
		self.head = None

	def visit(self):
		temp = self.head
		while temp!=None:
			print(temp.data)
			temp = temp.next	
	
	def push(self,data):
		temp = StackNode(data)
		temp.next = self.head
		self.head = temp
		self.top +=1

	def pop(self):
		if self.head == None:
			print("Underflow")
		temp = self.head
		self.head = temp.next
		temp = None
		self.top -=1

	def topElement(self):
		print(self.head.data)

	def size(self):
		print(self.top)		


if __name__ == '__main__':
    st = Stack()
    st.push(1)
    st.push(2)	
    st.push(3)	
    st.push(4)	
    st.push(5)	
    st.push(6)
    st.visit()
    st.pop()
    st.pop()	
    st.pop()		
    print("------------------------")
    st.visit()
    print("------------------------")
    
    st.topElement()
    st.size()

