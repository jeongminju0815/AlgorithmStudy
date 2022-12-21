from collections import deque, defaultdict

def bfs(graph, visited, row, col):
    visited[row][col] = True
    q = deque([[row, col]])
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    color = ""

    while q:
        r, c = q.popleft()

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if nx <0 or ny <0 or nx >= len(graph) or ny >= len(graph):
                continue
            if not visited[nx][ny] and graph[r][c] == graph[nx][ny]:
                color = graph[r][c]
                visited[nx][ny] = True
                q.append([nx,ny])
    
    return color

def c_bfs(graph, visited, row, col): #G ->R
    visited[row][col] = True
    q = deque([[row, col]])
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    color = ""
    while q:
        r, c = q.popleft()

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
   
            if nx <0 or ny <0 or nx >= len(graph) or ny >= len(graph):
                continue

            if not visited[nx][ny]:   
                if graph[r][c] == "B" and graph[nx][ny] == "B":
                    color = "B"
                    visited[nx][ny] = True
                    q.append([nx,ny])
                
                elif graph[r][c] == "B" or graph[nx][ny] == "B":
                    pass

                else:
                    color = "R"
                    visited[nx][ny] = True
                    q.append([nx,ny])
    return color



n = int(input())
graph = []
visited = [[False for i in range(n)] for i in range(n)]
visited2 = [[False for i in range(n)] for i in range(n)]

for i in range(n):
    graph.append(input())

color = defaultdict(int)
color2 = defaultdict(int)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:    
            color[bfs(graph, visited, i,j)] += 1

        if not visited2[i][j]:
            color2[c_bfs(graph, visited2, i,j)] += 1

print(sum(color.values()), sum(color2.values()))

