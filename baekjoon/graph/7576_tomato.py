from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
tomato = []
move = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 1:
            tomato.append((i,j))
            visited[i][j] = 1

def bfs(matrix):
    global tomato
    q = deque(tomato)
    while q:
        i, j = q.popleft()
        for x, y in move:
            dx = x + j
            dy = y + i
            if 0 <= dx < n and 0 <= dy < m:
                if matrix[dy][dx] == 0 and not visited[dy][dx]:
                    visited[dy][dx] = 1
                    matrix[dy][dx] = matrix[i][j] + 1
                    q.append((dy,dx))
def result():
    maxValue = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                print(-1)
                return
            elif matrix[i][j] > maxValue:
                maxValue = matrix[i][j]

    print(maxValue-1)
    return

bfs(matrix)
result()