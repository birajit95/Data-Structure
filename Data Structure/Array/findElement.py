# a = [i for i in range(1,11)]
a = [1,2,3,4,5]
index = 3
ranges = [[0,2],[0,3]]

def find(a, ranges, index):
	for item in ranges:
		left = item[0]
		right = item[1]
		temp = a[right]
		for i in range(right, left-1, -1):
			a[i]=a[i-1]
		a[left]=temp
	print(a[index])

find(a, ranges, index)

