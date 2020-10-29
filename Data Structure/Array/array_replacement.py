ar = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
# ar =[19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]

def replacement(ar):
	for i in range(0, len(ar)):
		if ar[i]!=-1:
			ar[i]=i
	return ar
print(replacement(ar))			