class Node:
	def __init__(self,data):
		self.data = data
		self.next = next

class CirclerList:
    def __init__(self):
        self.head = None

    def printf(self):
        temp = self.head.next
        temp2 = self.head.next

        while True:
             print(temp.data)
             temp=temp.next
             if temp == temp2:
                 break   

    def insertBeg(self,data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            temp.next = self.head
            return
        temp.next = self.head.next
        self.head.next = temp
        return  

    def insertEnd(self,data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            temp.next = self.head
            return
        temp.next = self.head.next
        self.head.next = temp
        self.head = temp        
    
    def insertAft(self,data,key):
    	temp = self.head.next
    	temp2 = self.head.next
    	while True:
    		flag = True
    		if temp.data == key:
    			break
    		temp = temp.next    	
    		if temp == temp2:
    		    flag = False
    		    break
    	if flag == True:
    	    temp3 = Node(data)
    	    temp3.next = temp.next
    	    temp.next=temp3
    	else:
    	    print('Key is not found')    	    

    def deleteBeg(self):
    	if self.head == None:
    		print("Empty List!")
    		return
    	if self.head.next == self.head:
    	    self.head = None
    	    # print("Nill if")
    	    return   
    	else:  
    	    temp = self.head.next
    	    self.head.next = temp.next
    	    temp = None
    	    return
    def deleteEnd(self):
        if self.head == None:
            print('list is empty')
            return
        if self.head.next==self.head:
            self.head = None
            return

        if self.head.next!=self.head:
            temp= self.head.next
            while True:
                temp=temp.next
                if(temp.next.next==self.head.next):
                    break
            temp.next=self.head.next
            self.head=temp
            return
    
    def sorted_insert(self,data):
        temp = Node(data)
        if self.head ==None:
            self.head=temp
            temp.next=self.head
            return
        if self.head.next==self.head:
            if(self.head.data<temp.data):
                temp.next=self.head
                self.head.next=temp
                self.head=temp
            else:
                temp.next=self.head
                self.head.next=temp
            return
        if self.head.next.data>temp.data:
            temp.next=self.head.next
            self.head.next=temp    

        else:
            tmp = self.head.next
            prev=self.head.next
            while(tmp.data<temp.data):
                prev=tmp
                tmp=tmp.next
                if(tmp.next==self.head.next):
                    break

                   
            if tmp==self.head:
                temp.next=self.head.next
                self.head.next=temp
                self.head=temp
            else:
                temp.next=prev.next
                prev.next=temp
    

    def check(self):
        print(self.head.data)
        print(self.head.next.data)
        print(self.head)
        print(self.head.next)
        print(self.head==self.head.next)


                
    	




if __name__ == '__main__':
        cl = CirclerList()
        cl.insertBeg(54);
        cl.insertBeg(29);
        cl.insertBeg(79);
        cl.insertBeg(69);
        cl.printf() 
        print("-------------------------------")   
        cl.insertEnd(205)
        cl.insertEnd(506)
        cl.printf()    
        print("-------------------------------")   
        cl.insertAft(400,69)
        cl.insertAft(98,54)
        cl.printf()
        print("-------------------------------") 
        # cl.deleteBeg()
        # cl.deleteBeg()
        print("-------------------------------") 
        cl.deleteEnd()
        cl.deleteEnd()
        cl.deleteEnd()
        cl.deleteEnd()
        cl.deleteEnd()
        cl.deleteEnd()
        cl.deleteEnd()
        cl.deleteEnd()
        cl.sorted_insert(5)
        cl.sorted_insert(6)
        cl.sorted_insert(1)
        cl.sorted_insert(20)
        cl.sorted_insert(4)
        cl.sorted_insert(7)
        cl.sorted_insert(3)
        cl.sorted_insert(8)
        cl.sorted_insert(8)
        cl.sorted_insert(9)
        cl.sorted_insert(11)
        cl.sorted_insert(12)
        cl.sorted_insert(7)
        cl.sorted_insert(25)
        cl.sorted_insert(14)
        cl.sorted_insert(19)
        cl.sorted_insert(4)
        cl.sorted_insert(9)
        cl.sorted_insert(17)

   



        cl.printf()
        print(")()()()((_(")
        cl.printf()


        print("-------------------------------") 
        print('checking........')
        print("-------------------------------") 

        cl.check()




