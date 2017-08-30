
def decorator(func):

	def wrapper(arg):
		print('before')
		func(arg)
		print('after')

	return wrapper

@decorator
def func(arg):
	print(arg)

func('hello')

