n = int(input())
temp = []

for i in range(n):
    k = int(input())
    temp.append(k)
temp.sort()

for i in temp:
    print(i)
