import sys
input = sys.stdin.readline
from collections import deque

def checkWall(i,j):
    for r,c in walls:
        if i <= r < i + a and j <= c < j + b:
            return False
    return True

def bfs():
    global start, end
    q = deque()
    visited[start[0]-1][start[1]-1] = 1
    q.append((start[0]-1,start[1]-1,0))
    while q:
        i,j,count = q.popleft()
        if i == end[0]-1 and j == end[1]-1:
            return count
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy <= n-a and 0 <= dx <= m-b:
                if not visited[dy][dx] and checkWall(dy,dx):
                    visited[dy][dx] = 1
                    q.append((dy,dx,count+1))
    return -1

n,m,a,b,k = map(int,input().split())
walls = []
visited = [[0] * m for _ in range(n)]
for _ in range(k):
    i,j = map(int,input().split())
    walls.append((i-1,j-1))
start = tuple(map(int,input().split()))
end = tuple(map(int,input().split()))

mx = [1,-1,0,0]
my = [0,0,1,-1]

print(bfs())