s = "abcd"
n = len(s)

def countSubStr(n):
	return n*(n+1)//2	


print(countSubStr(n))	


def fact(n):
	if n == 0:
		return 1
	return n*fact(n-1)

print(fact(4))


wordlist=["Save", "Water", "Save", "Yourself"]
words ="Save birajit"
wordlist=["welcome", "to", "geeks", "portal"]
words = "geeksforgeeks is a computer science portal for geeks to to"
def wordCount(words, wordlist):
	s = []
	ls = words.split(' ')
	for i in ls:
		if i in wordlist and i not in s:
			s.append(i)
	return s, len(s)

print(wordCount(words, wordlist))			
