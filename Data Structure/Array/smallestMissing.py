a = [0,0,0,1,1,1,2,3,3,5,6,7,9,10]
n = len(a)
m = 10

i = 0
while i<n:
	if(a[i+1]==a[i]+1):
		i+=1
	elif a[i] == a[i+1]:
		i+=1
	else:
		break	

print(a[i]+1)	
