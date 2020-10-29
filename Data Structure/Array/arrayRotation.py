a = [1,2,3,4,5,6,7]

def arrayRotate(a, d):
		temp = [a[i] for i in range(0, d)]
		for i in range(0,d):
			for j in range(d-i,len(a)-i):
				a[j-1] = a[j]
		for i in range(len(a)-d,len(a)):
			a[i] = temp[i-len(a)]
		return a
# print(arrayRotate(a,5))		

def reverse(a, x, y):
	while(x<y):
		temp = a[x]
		a[x]= a[y]
		a[y] = temp
		x+=1
		y-=1

def rotate(a,d):
	reverse(a,0, d-1)
	reverse(a, d, len(a)-1)
	reverse(a,0,len(a)-1)
	return a

print(rotate(a,5))


a = [i for i in range(1,31)]
def revreseArry(a):
	end = len(a)-1
	start = 0
	while(start<end):
		a[start], a[end] = a[end], a[start]
		start+=1
		end-=1
	return a
print(revreseArry(a))				
