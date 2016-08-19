x=50
def funcLocal():
	global x
	print('x равен', x)
	x=2
	print('Замена локального х на', x)
funcLocal()
print('x теперь равен', x)
