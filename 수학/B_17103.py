import math
def get_primary_list(n):
    array = [1 for _ in range(n+1)]

    for i in range(2, int(math.sqrt(n))+1):
        k = 2
        if array[i]:
            while k * i <= n:
                array[k*i] = False
                k+=1

    return array

n = int(input())
nums = [int(input()) for _ in range(n)]
max_num = max(nums)
primarys = get_primary_list(max_num)

for num in nums:
    result = 0

    for i in range(2, num // 2 + 1):
        if primarys[i] and primarys[num - i]:
            result += 1

    print(result)