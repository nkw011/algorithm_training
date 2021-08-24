import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [input().rstrip() for _ in range(n)]

moveX = [1,-1,0,0]
moveY = [0,0,1,-1]

def bfs1():
    visited = [[0] * n for _ in range(n)]
    q = deque()
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                value = matrix[i][j]
                visited[i][j] = 1
                q.append((i,j))
                count += 1
                while q:
                    r,c = q.popleft()
                    for index in range(4):
                        dx = c + moveX[index]
                        dy = r + moveY[index]
                        if 0 <= dy < n and 0 <= dx < n:
                            if not visited[dy][dx] and value == matrix[dy][dx]:
                                visited[dy][dx] = 1
                                q.append((dy,dx))
    return count

def bfs2():
    visited = [[0] * n for _ in range(n)]
    q = deque()
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                value = matrix[i][j]
                visited[i][j] = 1
                q.append((i,j))
                count += 1
                while q:
                    r,c = q.popleft()
                    for index in range(4):
                        dx = c + moveX[index]
                        dy = r + moveY[index]
                        if 0 <= dy < n and 0 <= dx < n:
                            if not visited[dy][dx]:
                                if value in ('R','G') and matrix[dy][dx] in ('R','G'):
                                    visited[dy][dx] = 1
                                    q.append((dy,dx))
                                elif value == matrix[dy][dx] == 'B':
                                    visited[dy][dx] = 1
                                    q.append((dy,dx))
    return count

result1 = bfs1()
result2 = bfs2()
print(result1, result2)