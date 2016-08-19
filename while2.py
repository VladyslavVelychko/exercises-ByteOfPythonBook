a=int(input())
b=int(input())
def gcd(a, b):
    return b and gcd(b, a%b) or a
print(int((a*b)/gcd(a,b)))
