a = [1, 2, 0, 4, 3, 0, 5, 0]
n = len(a)
count = 0
for i in a:
	if i !=0:
		a[count]=i
		count+=1
while(count<n):
	a[count]=0
	count+=1		

print(a)			
