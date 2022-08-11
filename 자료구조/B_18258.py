from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    cmd = input().split()
    length = len(queue)
    
    if cmd[0] == "push":
        queue.append(cmd[1])
        print(queue)
    if cmd[0] == "pop":
        if length == 0:
            print(-1)
        else:
            print(queue.popleft())
    if cmd[0] == "size":
        print(length)
    if cmd[0] == "empty":
        if length == 0:
            print(1)
        else:
            print(0)
    if cmd[0] == "front":
        if length == 0:
            print(-1)
        else:
            print(queue[0])
    if cmd[0] == "back":
        if length == 0:
            print(-1)
        else:
            print(queue[-1])