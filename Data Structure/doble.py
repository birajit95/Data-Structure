class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

class DoublyList:
     def __init__(self):
        self.head = None
        self.tail = None
     
     def printf(self):
     	temp = self.head
     	t3 = self.head
     	while(temp!=None):
     		print(temp.data)
     		t3=temp
     		temp=temp.next
     	print("Reversing")
     	while(t3!=None):
     	    # print(t3.data)
     	    t3=t3.prev
     	# print(self.tail.data)    	
     
     def insertBeg(self, data):
        temp = Node(data)

        if(self.head == None):
            self.head = temp
            self.tail = temp
            return

        temp2 = self.head
        temp2.prev = temp
        temp.next = temp2
        self.head = temp
        return

     def insertEnd(self, data):
     	temp = Node(data)
     	if self.head == None:
     		self.head = temp
     		self.tail = temp
     		return

     	temp.prev=self.tail
     	self.tail.next = temp
     	self.tail = temp
     	return	
    
     def reverse(self):
     	temp = self.head
     	while(temp!=None):
     		prev_ = temp.prev
     		next_ = temp.next
     		temp.next = prev_
     		temp.prev = next_
     		temp = next_
     	self.head = prev_.prev	





if __name__ == '__main__':
    dl = DoublyList()
    dl.insertBeg(1)
    dl.insertBeg(2)                   
    dl.insertBeg(3)                   
    dl.insertBeg(4)                   
    dl.insertBeg(5)                   
    dl.insertBeg(6)
    # dl.printf()
    print("+++++++++++++++++++++")
    dl.insertEnd(100)
    dl.insertEnd(200)               
    dl.insertEnd(300)               
    dl.insertEnd(400)               
    dl.insertEnd(500)               
    dl.insertEnd(600)
    dl.printf() 
    dl.reverse()
    print("After reverse")
    dl.printf() 


