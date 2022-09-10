n = int(input())

dp = [0, 1, 2, 4]

for i in range(4, 12):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
print(dp)

for i in range(len(dp)):
    k = int(input())
    print(dp[k])


