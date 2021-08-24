import sys
input = sys.stdin.readline
from collections import deque

def printMatrix(matrix):
    print()
    for array in matrix:
        print(array)
    print()

def bfs():
    global remain
    q = deque()
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q.append((0,0))
    count = 0
    while q:
        i,j = q.popleft()
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy < n and 0 <= dx < m:
                if not visited[dy][dx]:
                    if matrix[dy][dx] == 1:
                        visited[dy][dx] = 1
                        count += 1
                        matrix[dy][dx] = 0
                    else :
                        visited[dy][dx] = 1
                        q.append((dy,dx))
    return count

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
mx = [1,-1,0,0]
my = [0,0,1,-1]
remain = 0
timeCount = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            remain += 1
last = remain
            
while remain > 0:
    result = bfs()
    timeCount += 1
    if remain - result > 0:
        last = remain - result
    remain -= result
print(timeCount)
print(last)