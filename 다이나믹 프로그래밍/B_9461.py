n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [0] * max(arr)
dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(len(dp)-3):
    dp[i+3] = dp[i] + dp[i+1]

for i in arr:
    print(dp[i-1])