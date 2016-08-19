#Разбивка слов на 2 части, и переставление этих частей местами
s=input()
part1=0
part2=0
if len(s)%2==1:
    part1=s[:(int(len(s)/2))+1]
    part2=s[((int(len(s)/2))+1):]
else:
    part1=s[:((int(len(s)/2)))]
    part2=s[((int(len(s)/2))):]
    #print(part1)
    #print(part2)
print(part2+part1)
