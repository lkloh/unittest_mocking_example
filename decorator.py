
def my_decorator(my_func):
	def wrapper(name):
		return my_func(name)
	return wrapper

@my_decorator
def get_name(name):
   return name

print(get_name("John Doe"))