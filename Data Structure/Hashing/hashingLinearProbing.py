class Hash:
	def __init__(self, size):
		self.hash = [None]*size
		self.count = 0


	def insert(self, key):
		hash_func = key * 2 + 1
		index = hash_func % len(self.hash)
		size = len(self.hash)
		for i in range(0, len(self.hash)):
			if self.hash[(index+i)%size]==None:
				self.hash[(index+i)%size] = key
				self.count += 1
				break

	def search(self, key):
		hash_func = key * 2 + 1
		index = hash_func % len(self.hash)
		size = len(self.hash)


		for i in range(0, len(self.hash)):
			if self.hash[(index+i)%size]==key:
				print(key, " found")
				return
		print(key, ' Not found')
	
	def delete(self, key):
		hash_func = key * 2 + 1
		index = hash_func % len(self.hash)
		size = len(self.hash)
		

		for i in range(0, len(self.hash)):
			if self.hash[(index+i)%size]==key:
				self.hash[(index+i)%size] = None
				print(key, " is deleted")
				return
		print(key, ' Not found')

	def display(self):
		for i, key in enumerate(self.hash):
			if key !=None:
				print(self.hash[i], end = " ")


if __name__ == '__main__':
	h = Hash(10)
	h.insert(45)
	h.insert(15)
	h.insert(35)
	h.insert(4)
	h.insert(25)
	h.insert(3)
	h.insert(11)
	h.insert(112)
	h.insert(27)
	h.insert(57)
	# h.insert(57)
	

	h.display()
	print()
	print(h.hash)
	h.delete(4)
	print()
	print(h.hash)
    
	h.display()
