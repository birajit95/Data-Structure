a = [5,6,7,8,9,10,1,2,3,4]
ln = len(a)

def findPivot(a, low, high):
	if high<low:
		return -1
	if low == high:
		return low
	mid = (low+high)//2

	if mid<high and a[mid]>a[mid+1]:
		return mid
	elif mid>low and a[mid]<a[mid-1]:
		return mid-1
	if a[low]>=a[mid]:
		findPivot(a,low, mid-1)
	else:
		findPivot(a, mid+1, high)	

def search(a, key):
	pivot = findPivot(a, 0, ln-1)

	if pivot == -1:
		BinarySearch(a, 0, ln-1, key)	
	elif key>=a[0]:
		BinarySearch(a, 0, pivot-1, key)
	else:
		BinarySearch(a, pivot, ln-1, key)				
			
def BinarySearch(arr, low, high, key):
	if high < low:
		return -1
	mid = int((low + high)/2)
	if key == arr[mid]:
		return mid
	if key > arr[mid]:
		binarySearch(arr, (mid + 1), high, key);
	binarySearch(arr, low, (mid -1), key)

print(search(a,9))	