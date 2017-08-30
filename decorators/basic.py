
def decorator(func):

	def wrapper():
		print('before func call')
		func()
		print('after func call')

	return wrapper

@decorator
def random_function():
	print('random func')

random_function()


