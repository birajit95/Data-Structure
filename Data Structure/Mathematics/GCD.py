def GCD(x,y):
	for i in range(min(x,y),0,-1):
		if(x%i==0 and y%i==0):
			break
	return i		
		
def LCM(x,y):
	return int((x*y)/GCD(x,y))

print(GCD(12,144))
print(LCM(12,144))	

# import math

def LCM2(x,y):
	for i in range(min(x,y),x*y+1):
		if(i%x==0 and i%y==0):
			break
	return i
print(LCM2(12,144))			
			