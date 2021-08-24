import sys
input = sys.stdin.readline
from collections import deque

def bfs(r,c):
    q = deque()
    visited[r][c] = 1
    q.append((r,c))
    while q:
        i,j = q.popleft()
        if i == r2 and j == c2:
            return matrix[i][j]
        
        for index in range(6):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy < n and 0 <= dx < n:
                if not visited[dy][dx]:
                    matrix[dy][dx] = matrix[i][j] +1
                    visited[dy][dx] = 1
                    q.append((dy,dx))
    return -1

n = int(input().rstrip())
r1,c1,r2,c2 = map(int,input().split())
matrix = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
mx = [-1,1,-2,2,-1,1]
my = [-2,-2,0,0,2,2]
print(bfs(r1,c1))