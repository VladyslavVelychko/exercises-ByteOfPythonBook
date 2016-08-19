x=50
def funcLocal(x):
	print('x равен', x)
	x=2
	print('Замена локального х на', x)
funcLocal(x)
print('x по прежнему равен', x)
