
def decorator(func):

	def wrapper(func_arg):
		print('before')
		func(func_arg)
		print('after')

	return wrapper

@decorator
def func(func_arg):
	print(func_arg)

func('hello')

