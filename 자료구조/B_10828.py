import sys
input = sys.stdin.readline
n = int(input())

count = 0
arr = []

while count < n:
    count +=1
    cmd = input().split()
    
    length = len(arr)

    if cmd[0] == "push":
        arr.append(int(cmd[1]))
        
    elif cmd[0] == "empty":
        if length == 0:
            print("1")
        else:
            print("0")
    elif cmd[0] == "pop":
        if length == 0:
            print("-1")
        else:
            print(arr.pop())
    elif cmd[0] == "size":
        print(len(arr))    
    elif cmd[0] == "top":
        if length == 0:
            print("-1")
        else:
            print(arr[-1])
            
        
    