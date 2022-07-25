n,m = map(int,input().split())

def gcd(a,b):
    if a < b:
        a, b = b, a
    while a>0:
        b,a = a, b%a
    return b
def lcm(a,b,gcd):
    return int(a*b / gcd)
gcd = gcd(n,m)
print(gcd)
print(lcm(n,m,gcd))
