import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    k = int(input())
    if k == 0:
        if heap == []:
            print(0)
        else:
            num = heapq.heappop(heap)
            print(-num)
    else:
        heapq.heappush(heap, -k)