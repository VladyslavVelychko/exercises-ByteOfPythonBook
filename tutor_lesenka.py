#Program for output of numbers like lesenka
a=int(input())
sum=1
for i in range(2,a+2):
	print(sum)
	sum=str(sum)+str(i)
