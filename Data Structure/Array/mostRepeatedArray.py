a = [3, 4, 2, 3, 16, 3, 15, 16, 15, 15, 16, 2, 3]
# di = {i:a.count(i) for i in a}


# s = sorted(di, key = lambda x:di[x], reverse=True)
# print(s[:3])

p = [[None,1]]*10
# n = 1
# for i in range(0,len(a)):
# 	if i>10:
# 		break
# 	for j in range(0, n):
# 		print(i,j)
# 		if(a[i]==p[j][0]):
# 			flag = True
# 			break
# 		else:
# 			flag = False
# 	if flag == False:
# 		p[j][0]=a[i]
# 		p[j][1]=1
# 		n+=1
# 	else:
# 		p[i][1]+=1		
# print(p)	
a = [1,1,1,2,2,3,3,3,4,5]
x = sorted(a)
print(x)
c=0
for i in range(0, len(x)-1):
	if x[i]==x[i+1]:
		p[c][0] = x[i+1]
		p[c][1] += 1 
	else:
		c = c + 1
		p[c][0] = x[i+1]
	print(c)

print(p)		