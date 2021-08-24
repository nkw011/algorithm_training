# case가 없으면 return -1을 한다는 것을 빼먹었다.... 
# 아놔 이것땜에 계속틀렸고 고민했네...
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global minCount
    q = deque()
    visited[0][0] = [1] * (k+1)
    q.append((0,0,0,0))
    while q:
        i,j,count,h = q.popleft()
        if i == n-1 and j == m-1:
            return count
        if h < k:
            for index in range(8):
                dx = j + hmx[index]
                dy = i + hmy[index]
                if 0 <= dy < n and 0 <= dx < m:
                    if not visited[dy][dx][h+1] and matrix[dy][dx] == 0:
                        visited[dy][dx][h+1] = 1
                        q.append((dy,dx,count+1,h+1))
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy < n and 0 <= dx < m:
                if not visited[dy][dx][h] and matrix[dy][dx] == 0:
                    visited[dy][dx][h] = 1
                    q.append((dy,dx,count+1,h))
    return -1

k = int(input().rstrip())
m,n = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
minCount = (n * m) +1

mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]
hmx = [-2, -1, 1, 2, 2, 1, -1, -2]
hmy = [1, 2, 2, 1, -1, -2, -2, -1]
print(bfs())