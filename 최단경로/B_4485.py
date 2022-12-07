import heapq

INF = 1e9
def dijakstra(row, col, arr, result): #start = (row,)
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    q = []
    heapq.heappush(q, (arr[row][col], row, col))
    result[row][col] = arr[row][col]

    while q:
        s_cost, s_row, s_col = heapq.heappop(q) # 큐에 있는 가장 작은 비용과 해당 노드 출력

        for i in range(len(dx)):
            nx = s_row + dx[i] 
            ny = s_col + dy[i]
            if nx >= len(arr[0]) or ny >= len(arr[0]) or nx < 0 or ny < 0:
                continue
            
            _cost = result[s_row][s_col] + arr[nx][ny] # 넘어온 비용 + 현재 비용
            if _cost < result[nx][ny]:
                result[nx][ny] = _cost
                heapq.heappush(q, (result[nx][ny], nx, ny))

    return result       


n = 1
count = 0
while n!=0:
    n = int(input())
    if n==0:
        break
    count += 1
    arr = []
    result = []
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
        _temp = []
        for j in range(n):
            _temp.append(INF)
        result.append(_temp)
    result = dijakstra(0, 0, arr, result)
    print(f"Problem {count}: {result[n-1][n-1]}")
    
