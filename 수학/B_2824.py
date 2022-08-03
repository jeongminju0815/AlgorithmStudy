#14:21
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

def mul(temp):
    k = 1
    for i in temp:
        k*=i
    return k

def gcd(a,b):
    if a<b:
        a, b = b, a
    while a>0:
        b, a = a, b%a
    return b


result = str(gcd(mul(a),mul(b)))
if len(result) >9:
    print(result[-9:])
else:
    print(result)
