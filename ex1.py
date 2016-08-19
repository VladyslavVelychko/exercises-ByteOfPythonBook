def xo(s):
    sub1='o'
    count1=int(str.count(sub1,len(s)))
    sub2='x'
    count2=int(str.count(sub2,len(s)))
    if count1==count2:
        return true
    else:
        return false
xo('xoox')
print(count1)
print(count2)
