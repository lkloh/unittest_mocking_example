# https://stackoverflow.com/questions/5929107/decorators-with-parameters

def decorator(decorator_arg):

	def outer_wrapper(func):
		def inner_wrapper():
			print('before')
			return_val = func()
			assert return_val <= decorator_arg
			print('after')
		return inner_wrapper

	return outer_wrapper


@decorator(8)
def func():
	return 7

func()
