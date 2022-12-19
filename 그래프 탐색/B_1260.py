from collections import deque

def dfs(graph, visited, start):
    visited[start] = True
    print(start, end =" ")

    for i in sorted(graph[start]):
        if not visited[i]:
            dfs(graph, visited, i)
    return

def bfs(graph, visited, start):
    q = deque([start])
    visited[start] = 1

    while q:
        node = q.popleft()
        print(node, end =" ")
 
        for i in sorted(graph[node]):
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, visited, v)
visited = [False] * (n+1)
print()
bfs(graph, visited, v)