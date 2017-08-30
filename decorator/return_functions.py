
def parent(n):

	def first_func():
		return 'first'

	def second_func():
		return 'second'

	try:
		assert n == 10
		return first_func
	except:
		return second_func


func_10 = parent(10)
func_11 = parent(11)

print func_10()
print func_11()
