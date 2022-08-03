import sys
input = sys.stdin.readline
n = int(input())

money = []
for i in range(n):
    m = int(input())
    
    if m == 0:
        money.pop()
    else:
        money.append(m)
print(sum(money))
        