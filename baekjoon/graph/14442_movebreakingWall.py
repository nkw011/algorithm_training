import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def bfs():
    visited[0][0][0] = 1
    q = deque()
    q.append((0,0,0))
    while q :
        i,j,count= q.popleft()
        if i == n-1 and j == m-1:
            return visited[i][j][count]
        for idx in range(4):
            dy = i + my[idx]
            dx = j + mx[idx]
            if 0 <= dy < n and 0 <= dx < m:
                if matrix[dy][dx] == '1' and count < k and not visited[dy][dx][count+1]:
                    visited[dy][dx][count+1] = visited[i][j][count]+1
                    q.append((dy,dx,count+1))
                elif matrix[dy][dx] == '0' and not visited[dy][dx][count]:
                    visited[dy][dx][count] = visited[i][j][count] +1
                    q.append((dy,dx,count))
    return -1


n,m,k = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[[0] * 11 for _ in range(m)] for _ in range(n)]
my = [1,-1,0,0]
mx = [0,0,1,-1]
print(bfs())