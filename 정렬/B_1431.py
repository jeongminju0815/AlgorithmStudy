def sum(arr):
    count = 0
    for i in arr:
        if i.isdigit():
            count+=int(i)
    return count

n = int(input())
arr = []

for i in range(n):
    k = input()
    arr.append(k)
arr.sort()
arr.sort(key = lambda x : (len(x),sum(x)))

for i in arr:
    print(i)