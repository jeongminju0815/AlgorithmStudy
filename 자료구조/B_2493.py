n = int(input())
arr = list(map(int,input().split()))
stack = [] #최대값을 저장할 스택
result = [] #수신 탑 인덱스

for i in range(n):
    while stack:
        print(stack)
        if stack[-1][1] > arr[i]:
            result.append(stack[-1][0])
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append([i+1,arr[i]])
            
print(' '.join(map(str,result)))
        