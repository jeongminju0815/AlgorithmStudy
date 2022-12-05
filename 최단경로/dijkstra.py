import sys

input = sys.stdin.readline
INF = int(1e9)

n, m =map(int, input().split()) #n : 노드 개수, m : 간선 개수
start = int(input()) #시작 노드 번호
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node(): #어떤 노드가 짧을지 모두 탐색
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]: #시작 노드로 부터 업데이트
        distance[j[0]] = j[1]
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]: #현재 위치에서
            cost = distance[now] + j[1] #이동하는 경로를 계산해서
            if cost < distance[j[0]]: #더 짧다면
                distance[j[0]] = cost #업데이트

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])