
def parent(n):

	def first_func(arg):
		return 'first_func %d' % arg

	def second_func(arg):
		return 'second_func %d' % arg

	try:
		assert n == 10
		return first_func
	except:
		return second_func


func_10 = parent(10)
func_11 = parent(11)

print func_10(7)
print func_11(7)
