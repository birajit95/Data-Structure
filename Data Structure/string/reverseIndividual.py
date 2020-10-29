string = "My name is Birajit"

def reverse(string):
	strRev = ""
	ls = ""
	for i in string:
		if i !=" ":
			ls += i
		else:
			# strRev += ls[::-1]+' '
			for j in range(len(ls)-1,-1,-1):
				strRev += ls[j]
			strRev+=" "  
			ls = " "
	# strRev+=ls[::-1]
	for j in range(len(ls)-1,-1,-1):
			strRev += ls[j]	

	return strRev

print(reverse(string))

# for i in range(20,0,-1):
# 	print(i,end=" ")	