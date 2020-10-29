class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.counter = 0

	def printf(self):
		temp = self.head
		while temp!=None:
			print(temp.data)
			temp=temp.next


	def insert_Beg(self,data):
		temp = Node(data)
		temp.next = self.head
		self.head = temp
		# return self.head

	def insert_End(self,data):
		temp = Node(data)

		if self.head is None:
			self.head=temp
			return

		last = self.head
		while(last.next):
			last = last.next
		last.next = temp
			
	def insert_nth(self, data, pos):
		temp = Node(data)
		count = 1
		temp2 = self.head
		while(count<pos-1):
			count += 1
			temp2 = temp2.next
		temp.next = temp2.next	
		temp2.next = temp

	def insert_before(self, data, target):
		temp = Node(data)

		temp2 = self.head

		while(temp2.next.data!=target and temp2.next!=None):
			temp2 = temp2.next

		temp.next = temp2.next
		temp2.next = temp

	def insert_after(self, data, target):
		temp = Node(data)

		temp2 = self.head

		while(temp2.data!=target and temp2.next!=None):
			temp2 = temp2.next

		temp.next = temp2.next
		temp2.next = temp

	def delete_beg(self):
		if self.head == None:
			print('No data to be deleted')
		if self.head.next == None:
			temp = self.head
			self.head=None
			temp = None
		temp = self.head
		self.head = temp.next
		temp = None	

	def delete_end(self):
		temp = self.head
		while(temp.next.next!=None):
			temp = temp.next
		temp.next = None

	def delete_pos(self,pos):
		temp = self.head
		count = 1
		while(count<pos-1):
			count+=1
			temp = temp.next
		temp.next = temp.next.next

	def length(self):
		temp = self.head
		count = 0
		while(temp!=None):
			temp=temp.next
			count+=1
		print(f"Total {count}")	

	#length using recursive method
	def length_rec(self,node):
		if node==None:
			return 0
		return 1 + self.length_rec(node.next)

	#recursive search
	def search_rec(self, node, data):
		if node==None:
			return False
		if node.data==data:
			return True
		return self.search_rec(node.next, data)	
	def find_mid(self):
		temp = self.head
		temp2 = self.head
		while(temp!=None and temp.next!=None):
			temp=temp.next.next
			temp2 = temp2.next
		print(f'Mid {temp2.data}')

	def key_count(self, node, key):
		if node==None:
			return self.counter
		if key==node.data:
			self.counter+=1
		return self.key_count(node.next, key)

	def reverse(self):
		prev = None
		cur = self.head
		while(cur!=None ):
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		self.head = prev	

		








if __name__ == '__main__':
	lnk = LinkedList()
	lnk.insert_Beg(10)
	lnk.insert_Beg(12)
	lnk.insert_Beg(13)
	lnk.insert_Beg(11)
	lnk.insert_Beg(45)
	# lnk.printf()
	lnk.insert_End(20)
	lnk.insert_End(25)
	lnk.insert_End(27)
	lnk.insert_End(30)
	lnk.printf()
	lnk.insert_nth(100,5)
	print('____________________')
	# lnk.printf()
   
	print('____________________')
	lnk.insert_before(200,13)
	lnk.insert_before(2500,30)
	lnk.insert_after(4000,25)
	# lnk.printf()
	print("----------------------")
	lnk.delete_beg()
	lnk.delete_beg()

	# lnk.printf()
	lnk.delete_end()
	lnk.insert_End(30445)

	print("----------------------")

	lnk.printf()

	lnk.delete_pos(5)
	print("----------------------")
    
	lnk.printf()
	lnk.length()
	print(f'length {lnk.length_rec(lnk.head)}')
	print(lnk.search_rec(lnk.head, 27))
	lnk.find_mid()
	lnk.insert_End(20)
	lnk.insert_End(20)
	print(lnk.key_count(lnk.head,20))
	print("==================")

	lnk.printf()
	print("==================")
	lnk.reverse()
	lnk.printf()


	
    


	
					





		
