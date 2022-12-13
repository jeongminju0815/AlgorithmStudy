n = int(input())
arr = []

for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

count = 0
_start = 0
_end = 0

for i in arr:
    if i[0] >= _end:
        count+=1
        _end = i[1]

print(count)