def get_gcd(a,b):
    if a < b:
        a, b = b, a
    while a > 0:
        b, a = a, b%a
    return b

n , s = map(int,input().split())
arr = list(map(int,input().split()))

temp = []

for i in arr:
    temp.append(abs(s-i))

gcd = temp[0]
for i in range(1,len(temp)):
    gcd = get_gcd(gcd,temp[i])
print(gcd)