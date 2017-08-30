
def decorator(lower, upper):

	def outer_wrapper(func):

		def inner_wrapper(func_arg):
			print('before')
			val = func(func_arg)
			assert lower <= val
			assert val <= upper
			print('after')

		return inner_wrapper

	return outer_wrapper

@decorator(1, 100)
def func(arg):
	return arg * 7

func(8)
