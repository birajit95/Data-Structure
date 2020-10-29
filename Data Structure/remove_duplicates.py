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

	def insert_End(self,data):
		temp = Node(data)

		if self.head is None:
			self.head=temp
			return

		last = self.head
		while(last.next):
			last = last.next
		last.next = temp

	def removeDuplicates(self):
	    temp = self.head

	    while(temp.next):
	        if(temp.data==temp.next.data):
	             next_link = temp.next.next
	             temp.next=None
	             temp.next = next_link
	        else:
	             temp=temp.next     

	def get_to_end(self,key):
		temp2=self.head
		temp = self.head

		count = 0
		while temp2.next:
			temp2=temp2.next
			count += 1
			if(self.head.data==key):
				self.head = self.head.next
		i = 0
		while i<=count:
		    if (temp.data==key):
		    	temp2.next = temp
		    	next_link = temp.next
		    	temp.next = None
		    	temp = next_link
		    	temp2 = temp2.next
		    if temp.next.data == key:
		        temp2.next = temp.next
		        temp2 = temp2.next
		        next_link = temp.next.next
		        temp.next.next = None
		        temp.next = next_link
		    else:
		        temp = temp.next    	
		    i +=1	
		    	        	

if __name__=='__main__':
        l=LinkedList()
        l.insert_End(1)
        l.insert_End(2)
        l.insert_End(2)
        l.insert_End(2)
        l.insert_End(3)
        l.insert_End(4)
        l.insert_End(4)
        l.insert_End(4)
        l.insert_End(5)
        l.insert_End(5)
        l.insert_End(6)
        l.insert_End(7)
        l.printf()
        l.removeDuplicates()
        print("++++++++++++++++++++++++++++++++++++++")
        l.printf()
        print("++++++++++++++++++++++++++++++++++++++")
        
        lk = LinkedList()
        lk.insert_End(6)
        lk.insert_End(6)
        lk.insert_End(6)

        lk.insert_End(6)

        lk.insert_End(6)

        lk.insert_End(7)
        lk.insert_End(6)
        lk.insert_End(6)

        lk.insert_End(6)

        lk.insert_End(3)
        lk.insert_End(6)

        lk.insert_End(6)

        lk.insert_End(10)

        lk.printf()
        lk.get_to_end(6)
        print("+++++++++++++++++++hello+++++++++++++++++++")
        lk.printf()





