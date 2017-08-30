
def decorator(upper_bound, assert_stmt):

	def outer_wrapper(func):

		def inner_wrapper(func_arg):
			print('before')
			val = func(func_arg)
			assert_stmt(val, upper_bound)
			print('after')

		return inner_wrapper

	return outer_wrapper

def decorator_less_than(upper_bound):

	def assert_less_than(val, n):
		assert val <= n

	return decorator(upper_bound, assert_less_than)

def decorator_equal(upper_bound):

	def assert_equal(val, n):
		assert val == n

	return decorator(upper_bound, assert_equal)

# testing

@decorator_less_than(100)
def func_less_than(arg):
	return arg * 7

func_less_than(8)

@decorator_equal(56)
def func_equal(arg):
	return arg * 7

func_equal(8)





