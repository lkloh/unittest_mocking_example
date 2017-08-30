
def decorator(upper_bound, assert_stmt):

	def outer_wrapper(func):

		def inner_wrapper(func_arg, upper_bound):
			print('before')
			val = func(func_arg)
			assert_stmt(val, upper_bound)
			print('after')

		return inner_wrapper

	return outer_wrapper

def assert_less_than(val, n):
	assert val <= n

def assert_equal(val, n):
	assert val == n

@decorator(56, assert_less_than)
def func(arg):
	return arg * 7

func(8, assert_less_than)



