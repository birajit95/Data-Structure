a = [2,1,4,5,6,9,3,10,7,8]
l = 0;
h = 9

def mergeSort(a, l, h):
	if l<h:
		mid = (l+h)//2
		mergeSort(a, l, mid)
		mergeSort(a, mid+1, h)
		merge(a, l, mid, h)

def merge(a, l, mid, h):
	n1 = mid - l
	n2 = h - mid + 1
	L = [None]*n1
	R = [None]*n2


	for i in range(0, n1):
		L[i] = a[l+i]

	for j in range(0, n2):
		R[j] = a[mid+j]
	print(L)
	print(R)
	i = j = 0
	k = l
	while(i<n1 and j<n2):
		if(L[i]<=R[j]):
			a[k] = L[i]
			i+=1
		else:
			a[k] = R[j]
			j+=1
		k+=1
	while i<n1:
		a[k]=L[i]
		i+=1
		k+=1
	while j<n2:
		a[k]=R[j]
		j+=1
		k+=1
print(a)
mergeSort(a, l, h)
print(a)


