num = 12345

def sumOfDigit(num):
	sum = 0
	while num>0:
		x = num % 10
		sum = sum + x
		num = num // 10
	return sum
print(sumOfDigit(num))

def reverseNum(num, n):
	s = 0
	while(num>0):
		x = num % 10
		s = s + x*10**n
		num = num //10
		n = n-1
	return s

print(reverseNum(num,4))		