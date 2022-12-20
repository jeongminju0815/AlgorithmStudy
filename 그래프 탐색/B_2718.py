from collections import deque

def bfs(miro, visited, row, col):
    visited[row][col] = True
    result[row][col] = 1
    q = deque([[row, col]])
    
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    while q:
        r, c = q.popleft()

        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c
            rlength = len(miro)
            clength = len(miro[0])

            if nx <0 or ny <0 or nx >= rlength or ny >= clength:
                continue
            if not visited[nx][ny] and miro[nx][ny] != "0":
                q.append([nx, ny])
                visited[nx][ny] = True
                result[nx][ny] = result[r][c] + 1
    return 


n, m = map(int, input().split())
miro = []
result = [[0 for i in range(m)] for i in range(n)]

visited = [[False for i in range(m)] for i in range(n)]

for i in range(n):
    miro.append(input())


bfs(miro, visited, 0,0)
print(result[n-1][m-1])