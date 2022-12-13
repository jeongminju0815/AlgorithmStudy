import heapq

def dijakstra(start, arr):
    q = []
    heapq.heappush(q, (0, start))
    





sx, sy = map(float, input().split())
ex, ey = map(float, input().split())
n = int(input())

arr = []

for i in range(n):
    x, y = map(float, input().split())
    arr.append([x, y])

dijakstra(0, arr)