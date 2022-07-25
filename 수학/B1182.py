n, s = map(int,input().split())
arr = list(map(int,input().split()))
count = 0



def dfs(idx, list, k):
    if len(list) == k:
        answer.append(list[:])
        return

    for i in range(idx, n):       
        dfs(i+1,list+[arr[i]],k)

for i in range(1, n+1):
    answer = []
    dfs(0, [],i)
    for j in answer:
        if sum(j) == s:
            count+=1
print(count)