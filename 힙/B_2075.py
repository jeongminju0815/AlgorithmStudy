import heapq

n = int(input())
heap = []

for i in range(n):
    numbers = list(map(int, input().split()))
    if not heap:
        for n in numbers:
            heapq.heappush(heap, n)
    else:
        for n in numbers:
            if heap[0] < n:
                print(heapq.heappop(heap))
                heapq.heappush(heap, n)
print(heap[0])
