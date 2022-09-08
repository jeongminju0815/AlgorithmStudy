from collections import deque
from this import d

def dfs(start, graph, visited):
    graph[start] = sorted(graph[start])
    visited[start] = 1
    print(start, end=" ")
    for n in graph[start]:
        if visited[n] == 0:
            dfs(n, graph, visited)
    return 

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = 1

    while q:
        s = q.popleft()
        print(s, end=" ")
        for n in graph[s]:
            if visited[n] == 0:
                visited[n] = 1
                q.append(n)
            

n, m, v = map(int,input().split())

graph = [[] for i in range(1000+1)]


for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
dfs_visited = [0 for i in range(1000+1)]
bfs_visited = [0 for i in range(1000+1)]
dfs(v, graph, dfs_visited)
bfs(v, graph, bfs_visited)
