import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())
matrix = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[-1] * m for _ in range(n)] for _ in range(h)]
tomato = []
remain = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if matrix[k][i][j] == 1 :
                tomato.append((i,j,k))
                visited[k][i][j] = 0
            elif matrix[k][i][j] == 0 :
                remain += 1

moveX = [1,-1,0,0,0,0]
moveY = [0,0,1,-1,0,0]
moveZ = [0,0,0,0,1,-1]

def bfs():
    global remain
    q = deque(tomato)
    count = 0
    while q :
        i,j,k = q.popleft()
        for index in range(6):
            dx = j + moveX[index]
            dy = i + moveY[index]
            dz = k + moveZ[index]
            if 0 <= dz < h and 0 <= dy < n and 0 <= dx < m:
                if visited[dz][dy][dx] == -1 and matrix[dz][dy][dx] == 0:
                    visited[dz][dy][dx] = visited[k][i][j] + 1
                    count = max(visited[dz][dy][dx],count)
                    remain -= 1
                    q.append((dy,dx,dz))
    if remain != 0 :
        print(-1)
    elif not remain and len(tomato) == 0 :
        print(-1)
    else :
        print(count)
        
bfs()