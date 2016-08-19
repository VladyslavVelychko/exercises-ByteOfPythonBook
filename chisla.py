a=int(input())
b=int(input())
c=int(input())
if a<=b<=c:
	max=c
	min=a
	avg=b
elif a<=c<=b:
	max=b
	min=a
	avg=c
elif b<=a<=c:
	max=c
	min=b
	avg=a
elif b<=c<=a:
	max=a
	min=b
	avg=c
elif c<=a<=b:
	max=b
	min=c
	avg=a
elif c<=b<=a:
	max=a
	min=c
	avg=b
print(max)
print(min)
print(avg)
