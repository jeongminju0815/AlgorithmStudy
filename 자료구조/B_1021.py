from collections import deque
n, m = map(int,input().split())
arr = list(map(int,input().split()))


lst = [i for i in range(1,n+1)]
queue = deque(lst)
result = []
count = 0

for i in range(len(arr)):
    k = queue.index(arr[i])
    
    if (len(queue)//2) +1 > k :
        while queue[0] != arr[i]:
            queue.append(queue.popleft())
            count+=1
    
    else:
        while queue[0] != arr[i]:
            queue.appendleft(queue.pop())
            count+=1
    queue.popleft()
print(count)