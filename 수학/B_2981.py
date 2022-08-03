n = int(input())
arr = [int(input()) for i in range(n)]

arr.sort()
k = 1
temp = [-1] * len(arr)  
while k < arr[0] + 1:
    k +=1
    mod = arr[0] % k
    for i in range(1, len(arr)):
        if arr[i] % k == arr[0]:
            temp[i] = k
        if arr[i] % k != mod:
            break
        if i == len(arr)-1:
            print(k)
for i in range(2, len(temp)):
    j = temp[1]
    if temp[i] == -1 or temp[i] !=j:
        break
    if i == len(temp) -1:
        print(j)
        