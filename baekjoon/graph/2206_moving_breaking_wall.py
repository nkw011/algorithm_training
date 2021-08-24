import sys
input = sys.stdin.readline
from collections import deque
INF = 2500

n,m = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[[INF,INF] for _ in range(m)] for _ in range(n)]
mx = [1,-1,0,0]
my = [0,0,1,-1]

def bfs():
    q = deque()
    visited[0][0][0] = 1
    q.append((0,0,True))
    while q:
        i,j,able = q.popleft()
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if i == n-1 and j == m-1:
                return min(visited[i][j])
            if 0<= dy < n and 0 <= dx < m:
                if not visited[dy][dx][0] or not visited[dy][dx][1]:
                    if able:
                        if matrix[dy][dx] == '0':
                            visited[dy][dx][0] = visited[dy][dx][0] + 1
                            q.append((dy,dx,True))
                        else :
                            visited[dy][dx][1] = visited[dy][dx][0] + 1
                            q.append((dy,dx,False))
                    else :
                        if matrix[dy][dx] == '0':
                            visited[dy][dx][1] = visited[dy][dx][1] + 1
                            q.append((dy,dx,False))
    return -1 

print(bfs())