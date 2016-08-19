a=int(input())
if 11<=a<=20 or 211<=a<=220 or 311<=a<=320 or 411<=a<=420 or 511<=a<=520 or 611<=a<=620 or 711<=a<=720 or 811<=a<=820 or 911<=a<=920:
    print(str(a)+' программистов')
elif a==1 or a%100==1 or a%10==1:
	print(str(a)+' программист')
elif (a==2 or a%100==2 or a%10==2) or (a==3 or a%100==3 or a%10==3) or (a==4 or a%100==4 or a%10==4):
	print(str(a)+' программиста')
else:
	print(str(a)+' программистов')
