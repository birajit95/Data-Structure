a =[1,2,3,4,5,6,7,8,9,10]
def reverse(a):
	left = 0
	right = len(a)-1

	while(left<right):
		temp = a[left]
		a[left]=a[right]
		a[right]=temp
		right-=1
		left+=1
	return a
print(reverse(a))

s = "Hello Brother"
def reverseStr(s):
	
	# i = 0x`
	n = len(s)-1
	s2 = " "
	while(n>=0):
		x = n%10
		s2+=s[x]
		n=n-1
	return s2	

	
	


print(reverseStr(s))		