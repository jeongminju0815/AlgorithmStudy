import sys
input = sys.stdin.readline

sl = list(input().rstrip()) 
n = int(input())
sr = []

for i in range(n):
    cmd= input().split()
    
    if cmd[0] == "L":
        if sl:
            sr.append(sl.pop())
    if cmd[0] == "D":
        if sr:
            sl.append(sr.pop())
    if cmd[0] == "B":
        if sl:
            sl.pop()
    if cmd[0] == "P":
        sl.append(cmd[1])
sl.extend(reversed(sr))
print(''.join(sl))