from collections import deque

def bfs(graph, visited, row, col):
    count = 0
    visited[row][col] = True
    q = deque([[row,col]])
    count += 1

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    while q:
        r, c = q.popleft()

        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c
            length = len(graph[0])

            if nx < 0 or ny < 0 or nx >= length or ny >=length:
                continue

            if not visited[nx][ny] and graph[nx][ny] == "1":
                q.append([nx,ny])
                visited[nx][ny] = True
                count+=1
    return count

n = int(input())
map = []
visited = [[False for i in range(n)] for i in range(n)]

for i in range(n):
    map.append(list(input()))

result = []

for i in range(n):
    for j in range(n):
        if map[i][j] == "1" and not visited[i][j]:
            result.append(bfs(map, visited, i, j))

print(len(result))
for i in sorted(result):
    print(i)