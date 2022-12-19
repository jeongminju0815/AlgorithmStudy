# from itertools import combinations

# n, s = map(int, input().split())
# arr = list(map(int, input().split()))

# count = 0
# for i in range(1, n+1):
#     for c in list(combinations(arr, i)):
#         if sum(c) == s:
#             count+=1
# print(count)

import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def subset_sum(idx, sub_sum):
    global cnt

    if idx >= n:
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1
    
    # 현재 arr[idx]를 선택한 경우의 가지
    print("경우1 before",idx+1, sub_sum)
    subset_sum(idx+1, sub_sum)
    print("경우1 after",idx+1, sub_sum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지
    print("경우2 before",idx+1, sub_sum)
    subset_sum(idx+1, sub_sum - arr[idx])
    print("경우2 after",idx+1, sub_sum)

subset_sum(0, 0)
print(cnt)