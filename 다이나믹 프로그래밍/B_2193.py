n = int(input())

dp = [0] * (2**n)
dp[1] = 1
dp[2] = 2

for i in range(3, len(dp)):
    if not i & (i-1):
        dp[i] = dp[i//2] + 1
        
print(dp)
    

