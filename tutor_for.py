a=int(input())
sum1=0
sum2=0
for i in range(a-1):
	number=int(input())
	sum1+=number
for j in range(a+1):
	sum2+=j
print(sum2-sum1)
