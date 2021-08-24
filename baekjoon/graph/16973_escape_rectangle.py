import sys
input = sys.stdin.readline
from collections import deque

def checkWall(r,c):
    global wall
    for i, j in wall:
        if r <= i < r+h and c <= j < c+w:
            return False
    return True

def bfs():
    q = deque()
    visited[sr-1][sc-1] = 1
    q.append((sr-1,sc-1,0))
    while q :
        i,j, count = q.popleft()
        if i == fr-1 and j == fc-1:
            return count
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0<= dy <= (n-h) and 0 <= dx <= (m-w):
                if not visited[dy][dx] and checkWall(dy,dx):
                    visited[dy][dx] = 1
                    q.append((dy,dx,count+1))
    return -1

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
wall = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            wall.append((i,j))
h,w,sr,sc,fr,fc = map(int,input().split())
mx = [1,-1,0,0]
my = [0,0,1,-1]

print(bfs())