import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    result = 0
    visited = [[0] * m for _ in range(n)]
    q = deque()
    for i,j in ice2:
        if not visited[i][j]:
            result += 1
            visited[i][j] = 1
            q = deque()
            q.append((i,j))
            while q:
                r,c = q.popleft()
                for index in range(4):
                    dx = c + mx[index]
                    dy = r + my[index]
                    if 0 <= dy < n and 0 <= dx < m:
                        if not visited[dy][dx] and matrix[dy][dx] != 0:
                            visited[dy][dx] = 1
                            q.append((dy,dx))
    return result

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
mx = [1,-1,0,0]
my = [0,0,1,-1]
ice1 = []
ice2 = []
ice3 = []
remain = 0
timeCount = 0
possible = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] != 0:
            ice1.append((i,j))
            remain += 1

while remain :
    timeCount += 1
    for i,j in ice1:
        count = 0
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy < n and 0 <= dx < m:
                if matrix[dy][dx] == 0:
                    count += 1
        if count < matrix[i][j]:
            ice2.append((i,j))
            matrix[i][j] -= count
        else :
            remain -= 1
            ice3.append((i,j))
    for i,j in ice3:
        matrix[i][j] =0
    result = bfs()
    if result >= 2:
        possible = True
        break
    ice1 = ice2[:]
    ice2 = []
    ice3 = []

if possible:
    print(timeCount)
else :
    print(0)