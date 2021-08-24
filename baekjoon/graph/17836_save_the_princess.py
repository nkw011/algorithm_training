import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    visited[0][0] = [1,1]
    q.append((0,0,0,False))
    while q :
        i,j,count,hasSword = q.popleft()
        if i == n-1 and j == m-1:
            return count
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy < n and 0<= dx < m:
                if hasSword and not visited[dy][dx][1]:
                    visited[dy][dx][1] = 1
                    q.append((dy,dx,count+1,True))
                elif not hasSword and not visited[dy][dx][0]:
                    if matrix[dy][dx] == 0:
                        visited[dy][dx][0] = 1
                        q.append((dy,dx,count+1,hasSword))
                    elif matrix[dy][dx] == 2:
                        visited[dy][dx][1] = 1
                        q.append((dy,dx,count+1,True))
    return -1

n,m,t = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
mx = [1,-1,0,0]
my = [0,0,1,-1]

result = bfs()
if result != -1 and result <= t:
    print(result)
else :
    print("Fail")