
def print_function_return_value_decorator(should_print):
	def actual_decorator(func):
		def wrapper(*args, **kwargs):
			print(*args)
			if should_print:
				print("This is called third")
			return func(*args, **kwargs)
		print("This is called second")
		return wrapper
	print("This is called first")
	return actual_decorator

@print_function_return_value_decorator(True)
def get_name(name):
	return name

get_name("John Doe")
