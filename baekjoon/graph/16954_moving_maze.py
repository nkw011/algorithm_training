# pop을 할 때 index out of range가 되지 않게 조심
# pop을 하면서 기존 정보를 새로 갱신할 때 새로 갱신했던 정보가 사라지지 않도록 
# 갱신하는 부분을 따로 분리해서 할 수 있도록하면 될 것 같다.
# 오늘 이 문제를 통해 많은 것을 깨닫고 갑니다....

import sys
input = sys.stdinr.readline
from collections import deque

matrix = [list(input().rstrip()) for _ in range(8)]
wall = []
visited = [[0] * 8 for _ in range(8)]

mx = [1,-1,0,0,1,-1,1,-1]
my = [0,0,1,-1,-1,-1,1,1]

for i in range(8):
    for j in range(8):
        if matrix[i][j] == '#':
            wall.append((i,j))
            
def bfs():
    global wall,visited
    q = [(7,0)]
    visited[7][0] = 1
    q2 = deque()
    wall2 = deque()
    while q:
        q2 = deque(q)
        q = []
        while q2:
            r,c = q2.popleft()
            if (r,c) == (0,7):
                return 1
            if matrix[r][c] != '#':
                for index in range(8):
                    dx = c + mx[index]
                    dy = r + my[index]
                    if 0<= dy < 8 and 0 <= dx < 8:
                        if not visited[dy][dx] and matrix[dy][dx] != '#':
                            visited[dy][dx] = 1
                            q.append((dy,dx))
                q.append((r,c))
        wall2 = deque(wall)
        wall = []
        while wall2:
            r,c = wall2.popleft()
            matrix[r][c] = '.'
            if r+1 < 8:
                wall.append((r+1,c))
        # 원래는 있어야할 벽이 사라지는 경우가 생겨서
        # 벽을 넣는 코드를 따로 뺐다.
        for i,j in wall:
            matrix[i][j] = '#'
        # 제자리에 있을 경우 visited를 매번 초기화하지 않게되면
        # 앞으로 이동을 못하게 되는 경우가 있어서 visited를 할 때마다 초기화하였다.
        visited = [[0] * 8 for _ in range(8)]
    return 0

print(bfs())