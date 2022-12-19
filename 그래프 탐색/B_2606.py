from collections import deque

def bfs(graph, visited, start):
    visited[start] = 1
    q = deque([start])
    count = 0

    while q:
        node = q.popleft()

        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                count+=1
                q.append(i)
    return count



n = int(input())
e = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

print(bfs(graph, visited, 1))
