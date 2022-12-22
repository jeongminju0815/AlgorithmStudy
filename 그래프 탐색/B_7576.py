from collections import deque

def range_check(x,y,m,n):
    if 0<=x<m and 0<=y<n:
        return True
    return False

def bfs(tomato):
    total=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque(tomato)
    while queue:
        x,y,cnt=queue.popleft() # cnt에는 토마토가 몇초에 자랐는지에 대한 정보가 저장되어있음
        if cnt>total:
            total=cnt
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if range_check(nx,ny,m,n):
                if array[nx][ny] == 0:
                    array[nx][ny] = 1
                    queue.append([nx,ny,cnt+1]) # 토마토가 자란다
    return total
n,m=map(int,input().split())
array=[]
tomato = []
for i in range(m):
    tmp_array = list(map(int,input().split()))
    array.append(tmp_array)
    for j in range(n):
        if array[i][j] == 1:
            tomato.append([i,j,0])
answer=bfs(tomato)
for row in array: 
    if 0 in row: # 완료했는데 토마토가 자라지 않은 구역이 있는 경우
        answer=-1
print(answer)