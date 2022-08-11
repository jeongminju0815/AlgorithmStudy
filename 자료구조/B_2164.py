from collections import deque

n = int(input())

lst = [i for i in range(1,n+1)]
queue = deque(lst)

while len(queue) >= 2:
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue[0])