import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        print(stack)
        answer[stack.pop()] = A[i]
    stack.append(i)

print(stack)
print(*answer)