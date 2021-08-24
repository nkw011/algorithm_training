import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def bfs():
    q = deque()
    visited[hx-1][hy-1][0] = 1
    q.append((hx-1,hy-1,0,0))
    while q:
        i,j,count,flag = q.popleft()
        if i == ex-1 and j == ey-1:
            return count
        for index in range(4):
            dx,dy = j+mx[index],i+my[index]
            if 0 <= dy < n and 0 <= dx < m:
                if matrix[dy][dx] == 1:
                    if not flag and not visited[dy][dx][1]:
                        visited[dy][dx][1] = 1
                        q.append((dy,dx,count+1,1))
                else :
                    if not visited[dy][dx][flag]:
                        visited[dy][dx][flag] = 1
                        q.append((dy,dx,count+1,flag))
    return -1

n,m = map(int,input().split())
hx,hy = map(int,input().split())
ex,ey = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
mx,my = [1,-1,0,0],[0,0,1,-1]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]

print(bfs())