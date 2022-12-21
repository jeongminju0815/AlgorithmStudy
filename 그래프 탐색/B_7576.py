from collections import deque

def bfs(graph, visited, row, col):
    q = deque([[row, col]])

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c

            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue

            if graph[nx][ny] == 1:
                # print("1 : ", nx,ny)
                continue

            elif graph[nx][ny] == 0:
                # print("2: ", nx,ny)
                graph[nx][ny] = graph[r][c] + 1
                q.append([nx,ny])

            elif graph[nx][ny] != -1:
                # print("3 : ", nx,ny)
                if graph[nx][ny] < graph[r][c] + 1:
                    continue

                graph[nx][ny] = graph[r][c] + 1
                q.append([nx,ny])


m, n = map(int,input().split()) 
tomato = []
live = []
notlive = []
visited = [[False for i in range(m)] for i in range(n)]

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            live.append([i,j])
        if temp[j] == 0:
            notlive.append([i,j])
    tomato.append(temp)


if len(live) == 0:
    print(-1)
else:
    for i in range(len(live)):
        bfs(tomato, visited, live[i][0], live[i][1])

tmax = -1
flag = False

for i in notlive:
    if tomato[i[0]][i[1]] == 0:
        flag = True
        break
    if tomato[i[0]][i[1]] > tmax:
        tmax = tomato[i[0]][i[1]]

if flag:
    print(-1)
else:
    print(tmax-1)
