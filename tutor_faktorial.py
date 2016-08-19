n=int(input())
sum=1
sum1=1
sum2=0
for i in range(1,n+1):
	sum*=i
for j in range(1,n):
	sum1*=j
	sum2+=sum1
print(sum+sum2)
