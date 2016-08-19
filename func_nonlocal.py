def func_out():
	x=2
	print('x равен',x)
	def func_in():
		nonlocal x
		x=5
	func_in()
	print('Локальное х сменилось на',x)
func_out()
