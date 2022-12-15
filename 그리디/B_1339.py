from collections import defaultdict

n = int(input())
arr = []

for i in range(n):
    arr.append(input())

num = defaultdict(int)

for i in arr:
    for j in range(len(i)):
        num[i[j]] += 10 ** (len(i)-j-1)
length = len(num)
num1 = sorted(num.items(), key = lambda x:x[1])

start = 9- length +1

total = 0
for key, value in num1:
    num[key] = start
    start+=1

for i in arr:
    for j in range(len(i)):
        total += num[i[j]] * 10 ** (len(i) -j -1) 

print(total)