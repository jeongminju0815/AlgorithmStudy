import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m, x = map(int, input().split())

graph = [[] for i in range(n+1)]
result = [[INF for j in range(n+1)] for i in range(n+1)]
for i in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append([cost, end])

def dijakstra(start):
    q = []
    heapq.heappush(q, (0, start))
    result[start][start] = 0

    while q:
        cost, node = heapq.heappop(q)
        if result[start][node] < cost:
            continue
        for c, n in graph[node]:
            _cost = c + result[start][node]
            
            if _cost < result[start][n]:
                result[start][n] = _cost
                heapq.heappush(q, (_cost, n))

for i in range(1,n+1):
    dijakstra(i)

maxnum = -1
for i in range(1,len(result[x])):
    if i == x:
        continue
    if maxnum < result[x][i] + result[i][x]:
        maxnum = result[x][i] + result[i][x]
print(maxnum)
    

