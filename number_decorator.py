
def number_decorator(arg_number):
    def actual_decorator(func):
        def call_unit_test(*args, **kwargs):
            my_number = 7
            lucky_number = func(*args, **kwargs)
            assert lucky_number == arg_number
            return lucky_number
        return call_unit_test
    return actual_decorator


@number_decorator(42)
def get_magic_number():
	return 42

get_magic_number()
