# n = int(input())

# dp = [0] * (n+1)

# for i in range(2, len(dp)):
#     dp[i] = dp[i-1] + 1
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[int(i/3)] + 1)
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[int(i/2)] + 1)
# print(dp[n])
n = int(input())

dp = [0, 0, 1, 1] + [0] * (n+1)

for i in range(4, len(dp)):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[int(i//3)] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[int(i//2)] + 1)
print(dp[n])
        