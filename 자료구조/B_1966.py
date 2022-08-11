import sys
from collections import deque

input = sys.stdin.readline
test = int(input())

for i in range(test):
    case = input().split()
    arr = list(map(int,input().split()))
    queue = deque(arr)
    print(queue)
    
    temp = [j for j in range(int(case[0]))]
    sequeue = deque(temp)

    count = 0

    while True:
        if queue[0] == max(queue):
            if sequeue[0] == int(case[1]):
                count+=1
                print(count)
                break
            else:
                queue.popleft()
                sequeue.popleft()
                count+=1
        else:
            queue.append(queue.popleft())
            sequeue.append(sequeue.popleft())

        
            