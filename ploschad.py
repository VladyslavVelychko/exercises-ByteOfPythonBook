a=str(input())
if a=='треугольник':
	b=int(input())
	c=int(input())
	d=int(input())
	p=(b+c+d)/2
	s=(p*(p-b)*(p-c)*(p-d))**(1/2)
	print(s)
if a=='прямоугольник':
	b=int(input())
	c=int(input())
	print(b*c)
if a=='круг':
	b=int(input())
	print(3.14*(b**2))
