arr = list(map(int,input().split()))
temp = sorted(arr)
while arr != temp:
    for i in range(4):
        if arr[i] >= arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            continue
        print(' '.join(map(str,arr)))
    