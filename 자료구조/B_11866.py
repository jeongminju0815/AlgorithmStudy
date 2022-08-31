from collections import deque

n, k = map(int,input().split())
arr = [i for i in range(1,n+1)]
q = deque(arr)
print("<",end="")

while q:
    for i in range(k-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(),end='')
    
    if q:
        print(", ",end='')
print(">")