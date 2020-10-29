a1= [10, 5, 2, 23, 3,19]
a2 = [19, 5, 2]

def isSubset(a1,a2):
	flag = [False]*len(a2)
	for i in range(0, len(a2)):
		for j in range(0,len(a1)):
			if a2[i] == a1[j]:
				flag[i] = True
				break	
	return flag
				
print(isSubset(a1, a2))


def isSubset2(a1,a2):
	m = len(a1)
	n = len(a2)

	a1.sort()
	a2.sort()
	i = j = 0
	while(i<m and j<n):
		if a1[i]>a2[j]:
			j+=1
		if a1[i]==a2[j]:
			i+=1
			j+=1
		else:
			i+=1
	return False if i < m else True
  
				
print(isSubset2(a1, a2))