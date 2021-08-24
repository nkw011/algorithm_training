import sys
input = sys.stdin.readline
from collections import deque 

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
mx = [1,-1,0,0]
my = [0,0,1,-1]
start = (0,0)
possible = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            start = (i,j)
            possible = True
            break
    if possible :
        break
        
def bfs():
    global start
    q = deque()
    visited[start[0]][start[1]] = 1
    q.append(start)
    while q:
        i,j = q.popleft()
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy < n and 0 <= dx < m:
                if not visited[dy][dx] and matrix[dy][dx] != 0:
                    visited[dy][dx] = visited[i][j] + 1
                    q.append((dy,dx))
                    
bfs()
for i in range(n):
    for j in range(m):
        if visited[i][j] != 0:
            print(visited[i][j]-1,end=' ')
        else :
            print(visited[i][j],end=' ')
    print()