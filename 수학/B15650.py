n, m = map(int, input().split())

answer = []

def dfs(idx, temp):
    if len(temp) == m:
        answer.append(temp)
        return

    for i in range(idx, n):  
        dfs(i+1,temp+[i+1])

dfs(0, [])
for i in answer:
    print(" ".join(str(s) for s in i))