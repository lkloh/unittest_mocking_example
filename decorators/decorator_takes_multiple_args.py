
def decorator(arg1, arg2):

	def outer_wrapper(func):

		def inner_wrapper():
			print 'before'
			val = func()
			assert arg1 <= val
			assert val <= arg2
			print 'after'

		return inner_wrapper

	return outer_wrapper

@decorator(1, 100)
def random_func():
	return 7

random_func()





