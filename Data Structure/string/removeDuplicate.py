s = "aaabbbaccd"

def removeduplicate(s):
	st = s[0]
	for i in range(0,len(s)-1):
		if s[i] not in st:
			st+=s[i]
	return st
	
print(removeduplicate(s))	

