from itertools import combinations

n, m = map(int, input().split())
arr = []
chicken = [] #치킨집 좌표
home = [] # 집 좌표

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append([i,j])
        if arr[i][j] == 1:
            home.append((i,j))

ccombi = list(combinations(chicken, m))
ctotal = []

for i in range(len(ccombi)): #치킨집 경우의 수
    total = 0
    for j in range(len(home)): #모든 집
        temp = 200
        for k in range(m): #치킨집 m개
            d = abs(home[j][0] - ccombi[i][k][0]) + abs(home[j][1] - ccombi[i][k][1])
            if d < temp:
                temp = d
        total += temp
    ctotal.append(total)

print(min(ctotal))

        

