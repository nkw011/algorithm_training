# 불이 꼭 한 군데에서만 나오는 게 아니라는 것을 못봤다..
# 더 빨리 구현할려면 visited를 한 군데만 구현해서 fire와 jh를 동시에 이동가능하도록 하면 될 것 같다.
# 두번째로 jh와 fire를 찾을 때 미리 q에 집어넣으면 더 빠를 것 같기도 하다...

import sys
input = lambda : sys.stdin.readline()
from collections import deque

def bfs():
    global jh,fire
    q = deque()
    for i,j in fire:
        q.append((i,j,1,0))
        visited2[i][j] = 1
    q.append((jh[0],jh[1],0,0))
    visited[jh[0]][jh[1]] = 1
    while q:
        i,j,flag,count = q.popleft()
        if flag == 0 and (i == 0 or i == r-1 or j == 0 or j == c-1):
            return count +1
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy < r and 0 <= dx < c:
                if matrix[dy][dx] == '.':
                    if flag and not visited2[dy][dx]:
                        visited2[dy][dx] = 1
                        matrix[dy][dx] = 'F'
                        q.append((dy,dx,1,count+1))
                    elif not flag and not visited[dy][dx]:
                        visited[dy][dx] = 1
                        q.append((dy,dx,0,count+1))
    return "IMPOSSIBLE"

r,c = map(int,input().split())
matrix = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
visited2 = [[0] * c for _ in range(r)]
mx = [1,-1,0,0]
my = [0,0,1,-1]
jh = (0,0)
fire = []
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'J':
            jh = (i,j)
        elif matrix[i][j] == 'F':
            fire.append((i,j))
print(bfs())