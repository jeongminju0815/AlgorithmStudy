import sys

input = sys.stdin.readline
testcase = int(input())

for t in range(testcase):
    n = int(input())
    arr = []
    count = 0
 
    for i in range(n):
        s1, s2 = map(int, list(map(int,input().split())))
        arr.append([s1,s2])

    arr.sort()
    temp = arr[0][1]

    for i in arr:
        if i[1] <= temp:
            count+=1
            temp = i[1]
    print(count)

    
    
    