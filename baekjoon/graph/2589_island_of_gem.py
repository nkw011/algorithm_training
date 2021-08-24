import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global maxCount
    visited[start[0]][start[1]] = 1
    q = deque()
    q.append((start[0],start[1],0))
    while q:
        r,c,count = q.popleft()
        for index in range(4):
            dx = c + mx[index]
            dy = r + my[index]
            if 0 <= dy < n and 0<= dx < m:
                if not visited[dy][dx] and  matrix[dy][dx] =='L':
                    visited[dy][dx] = 1
                    q.append((dy,dx,count+1))
                    maxCount = max(count+1,maxCount)

n,m = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
mx = [1,-1,0,0]
my = [0,0,1,-1]
maxCount = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'L':
            visited = [[0] * m for _ in range(n)]
            bfs((i,j))
print(maxCount)