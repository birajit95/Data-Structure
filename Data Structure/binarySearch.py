a = [i for i in range(1,21)]
print(a)

def binarySearch(a,key):
	l = 0
	u = len(a)-1
	while(l<=u):
		mid = (l+u)//2
		if a[mid]==key:
			return 1
		elif(a[mid]>key):
			u=mid-1
		elif(a[mid]<key):
			l=mid+1
	return -1

print(binarySearch(a))
						