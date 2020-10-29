class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Hash:
	def __init__(self, size):
		self.hash = [None]*size


	def insert(self, key):
		hash_func = 2*key+1
		index = hash_func % len(self.hash)
		temp = Node(key)

		if(self.hash[index]==None):
			self.hash[index]=temp
			return
		temp.next = self.hash[index]
		self.hash[index] = temp

	def search(self, key):
		hash_func = 2*key+1
		index = hash_func % len(self.hash)

		temp = self.hash[index]

		while(temp):
			if temp.data == key:
				print(key,' found')
				return
			temp = temp.next	
		print(key,' Not Found')

	def delete(self, key):
		hash_func = 2*key+1
		index = hash_func % len(self.hash)
		temp = self.hash[index]

		if self.hash[index].data == key:
			self.hash[index] = self.hash[index].next
			return
		while temp:
			if temp.data ==  key:
				prev.next = temp.next
				break
			prev = temp	
			temp = temp.next
		if temp is None:
			print('Key not found')
			return
		temp = None	



	def display(self):
		for i in self.hash:
			if i is not None:
				temp = i
				while(temp):
					print(temp.data, end=" ")
					temp = temp.next	

if __name__ == '__main__':
		h = Hash(10)
		h.insert(12)
		h.insert(11)
		h.insert(2)
		h.insert(19)
		h.insert(7)
		h.insert(41)
		h.insert(18)
		h.insert(24)
		h.insert(25)
		# h.search(12)
		# h.search(1)	
		print("display")
		h.display()
		h.delete(245)
		print()
		h.display()



		
