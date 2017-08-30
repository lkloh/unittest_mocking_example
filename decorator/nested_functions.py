
def parent():
	print('parent')

	def first_child():
		return 'first child'

	def second_child():
		return 'second child'

	print(first_child())
	print(second_child())

parent()
