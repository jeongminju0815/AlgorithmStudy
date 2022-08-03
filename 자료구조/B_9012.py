import sys
input = sys.stdin.readline
n = int(input())


for i in range(n):
    vps = input()
    check = []
    
    for j in range(len(vps)):
        if vps[j] == "(":     
            check.append(1)
        elif vps[j] == ")":
            if check == []:
                print("NO")
                break
            else: check.pop()
        elif j == len(vps)-1:
            if check == []:
                print("YES")
            else:
                print("NO")
  
    
    