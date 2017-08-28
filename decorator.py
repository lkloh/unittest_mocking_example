
# https://stackoverflow.com/questions/10176226/how-to-pass-extra-arguments-to-python-decorator
# https://stackoverflow.com/questions/14703310/how-can-i-get-a-python-decorator-to-run-after-the-decorated-function-has-complet

def print_function_return_value_decorator(decorator_args):
	def actual_decorator(func):
		def wrapper(*args, **kwargs):
			if decorator_args:
				print("Decorator args are %s" % str(decorator_args))
				#print(*args)
			invoke_unit_test = func(*args, **kwargs)
			print('After the get_name was called!')
			return invoke_unit_test
		print('inside actual_decorator')
		return wrapper
	print("Before get_name")
	return actual_decorator

def number_decorator(arg_number):
    def actual_decorator(func):
        def call_unit_test(*args, **kwargs):
            my_number = 7
            lucky_number = func(*args, **kwargs)
            assert lucky_number == arg_number
            return lucky_number
        return call_unit_test
    return actual_decorator

@print_function_return_value_decorator("Whizz Bang")
def get_name(name):
	print("\n<get_name> You just did something inside get_name! <get_name>\n")
	return name

@number_decorator(42)
def get_magic_number():
	return 42

get_name("John Doe")

print "\n\n\n ****************\n   LUCKY NUMBER\n ****************\n"
get_magic_number()
