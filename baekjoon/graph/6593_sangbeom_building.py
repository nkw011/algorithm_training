# 이렇게 입력이 거지같은 문제는 처음보았다.

import sys
input = sys.stdin.readline
from collections import deque

mx = [1,-1,0,0,0,0]
my = [0,0,1,-1,0,0]
mz = [0,0,0,0,1,-1]

def bfs(start):
    k,r,c = start
    q = deque()
    visited[k][r][c] = 1
    q.append((k,r,c,0))
    while q:
        z,i,j,count = q.popleft()
        for index in range(6):
            dx = j + mx[index]
            dy = i + my[index]
            dz = z + mz[index]
            if 0 <= dz < L and 0 <= dy < R and 0 <= dx < C:
                if not visited[dz][dy][dx]:
                    if matrix[dz][dy][dx] == 'E':
                        return count +1
                    elif matrix[dz][dy][dx] == '.':
                        visited[dz][dy][dx] = 1
                        q.append((dz,dy,dx,count+1))
    return -1

while True:
    L,R,C = map(int,input().split())
    if L == 0 and R == 0 and C == 0:
        break
    count,rowCount = 0,0
    matrix = []
    row = []
    while count < L:
        inputs = input().rstrip()
        if inputs == '':
            continue
        row.append(list(inputs))
        rowCount += 1
        if rowCount == R:
            count += 1
            rowCount = 0
            matrix.append(row[:])
            row = []
    
    visited = [[[0]*C for l in range(R)] for _ in range(L)]
    S = (0,0,0)
    find = False
    for k in range(L):
        for i in range(R):
            for j in range(C):
                if matrix[k][i][j] == 'S':
                    S = (k,i,j)
                    find = True
                    break
            if find:
                break
        if find:
            break
    result = bfs(S)
    if result == -1:
        print("Trapped!")
    else :
        print("Escaped in {0} minute(s).".format(result))
    input().rstrip()