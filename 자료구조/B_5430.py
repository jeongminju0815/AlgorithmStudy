import re
test = int(input())

for t in range(test):
    p = input()
    n = int(input())
    
    arr = list(input()[1:-1].split(","))
    
    for i in range(len(p)):
        if n == 0:
            print("error")
            break
        if p[i] == "R":
            arr.reverse()
        if p[i] == "D":
            if len(arr) == 0:
                print("error")
                break
            else:
                arr = arr[1:]
    
    print("[" + ",".join(arr)+"]")