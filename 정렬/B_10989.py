import sys
input = sys.stdin.readline

n = int(input())
temp = [0] * 10001

for i in range(n):
    k = int(input())
    temp[k] += 1

for i in range(1, len(temp)):
    if temp[i] != 0:
        for j in range(temp[i]):
            print(i)