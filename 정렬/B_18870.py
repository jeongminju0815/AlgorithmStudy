n = int(input())
arr = list(map(int, input().split()))

set_arr = list(set(arr))
set_arr.sort()

result = {set_arr[i] : i for i in range(len(set_arr))}

for i in arr:
    print(result[i], end=' ')
    
