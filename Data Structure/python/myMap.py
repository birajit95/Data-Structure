# def myMap(func, l):
# 		yield [func(i) for i in l]

# for i in myMap(lambda x:x*x, [1,2,3,4,5,6]):
# 	print(i)


# def multiply(x):
# 	def mul(y):
# 		return x*y
# 	return mul

# mul3 = multiply(3)
# mul5 = multiply(5)
# print(mul3(7))
# print(mul5(7))

# from functools import wraps

# def dec(func):
# 	@wraps(func)
# 	def inner(*args, **kwargs):
# 		print("This is awesome function")
# 		return func(*args, **kwargs)
# 	return inner

# @dec			
# def fun1(a):
# 	print(f"This is func1 {a}")	

# # fun1 = dec(fun1)
# fun1(5)	
# print(fun1.__name__)



# def decorator(function):
# 	@wraps(function)
# 	def wraper(*args, **kwargs):
# 		print(f"You are calling {function.__name__} function")
# 		print(function.__doc__)
# 		return function(*args, **kwargs)
# 	return wraper	
# @decorator
# def add(a,b):
# 	"""This function takes 2 arguments and returns their sum"""
# 	return a+b

# @decorator
# def multiply(a,b):
# 	"""This function takes 2 arguments and returns their product"""
# 	return a*b	

# print(multiply(10,30))



#==========================================
from functools import wraps
import time
def deco(function):
	@wraps(function)
	def wraper(*args, **kwargs):
		t1 = time.time()
		fun = function(*args, **kwargs)
		t2= time.time()
		print(t2-t1)
		return fun
	return wraper

@deco	
def fun():
	l = [i for i in range(10000000)]
	# return l

fun()	




