import math
n = int(input())

arr = [int(input()) for i in range(n)]

temp = [0] * 10001
temp[0] = 1
temp[1] = 1

for i in range(2, int(math.sqrt(10000))+1):
    k = 2
    while k * i <= 10000:
        temp[k*i] = 1
        k+=1


for i in arr:
    k = int(i/2)
    
    if temp[k] == 0:
        print(k,k)
        
    else:
        for j in range(1,k-1):
            if temp[k-j] == 0 and temp[k+j] == 0:
                print(k-j,k+j)
                break
               
        