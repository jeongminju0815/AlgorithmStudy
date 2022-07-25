import math

arr = []
while True:
    n = int(input())
    if n==0:
        break
    arr.append(n)

# 입력 받은 값 중 가장 큰 값까지 에라토스테네스의 채로 소수 확인
arr_max = max(arr) 

temp = [0] * ((2*arr_max)+1)

for i in range(2, int(math.sqrt(2*arr_max))+1):
    k = 2
    while k * i <=2*arr_max:
        temp[k*i] = 1
        k+=1

for i in range(len(arr)):
    count = 0
    # 입력 받은 값마다 n+1 ~ 2n 범위에서 소수 개수 찾기
    for j in range(arr[i]+1,2*arr[i]+1):
        if temp[j] == 0:
            count+=1
    print(count)

