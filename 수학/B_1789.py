import math
n = int(input())

s = 0 # 1~k 의 합을 저장하는 변수
k = 1
while s <= n:
    s += k
    if s > n:
        break
    k += 1
print(k-1)