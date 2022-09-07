n = int(input())

# fibonacci(0) = 0, fibonacci(1) = 1, 
# fibonacci(2) = fibonacci(1) + fibonacci(0)
# fibonacci(3) = fibonacci(2) + fibonacci(1)
arr = []
if n == 0:
    print(1, 0)
else:
    for i in range(n):
        k = int(input())
        arr.append(k)
    temp = arr.copy()
    temp.sort()
    
    if n == 1 and k == 0:
        print(1, 0)
    
    else:
        dp = [[0,0]] * (temp[-1]+1)
        dp[0] = [1,0]
        dp[1] = [0,1]

        for i in range(2, len(dp)):
            dp[i] = [dp[i-1][0] + dp[i-2][0],  dp[i-1][1] + dp[i-2][1]]
            

        for i in arr:
            print(dp[i][0], dp[i][1])

