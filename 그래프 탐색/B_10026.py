import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def range_check(x,y,n,m):
    if 0<=x<n and 0<=y<n:
            return True
    return False

def dfs(x,y):
    #현재 색상 좌표를 방문해준다.
    visited[x][y] = True
    current_color = array[x][y]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if range_check(nx,ny,n,n):
            #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if visited[nx][ny]==False:
                if array[nx][ny] == current_color:
                    dfs(nx,ny)

n = int(input())
array = []

for i in range(n):
    array.append(list(input().rstrip()))

three_cnt, two_cnt = 0, 0

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if visited[i][j]==False:
            dfs(i,j)
            three_cnt += 1

for i in range(n): # R을 G로 바꾸어준다. --> 적록색약은 같은 색으로 보기 때문에
    for j in range(n):
        if array[i][j]=='R':
            array[i][j]='G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt,two_cnt)