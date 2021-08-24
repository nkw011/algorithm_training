import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global start,fire
    visited = [[0] * w for _ in range(h)]
    visited2 = [[0] * w for _ in range(h)]
    q = [start]
    q2 = deque()
    fireTemp = deque()
    visited2[start[0]][start[1]] = 1
    timeCount = 0
    while q:
        timeCount += 1
        fireTemp = deque(fire)
        fire = []
        while fireTemp:
            i,j = fireTemp.popleft()
            for index in range(4):
                dx = j + mx[index]
                dy = i + my[index]
                if 0 <= dy < h and 0 <= dx < w:
                    if not visited[dy][dx] and matrix[dy][dx] != '#':
                        visited[dy][dx] = 1
                        matrix[dy][dx] = '*'
                        fire.append((dy,dx))
        q2 = deque(q)
        q = []
        while q2:
            i,j = q2.popleft()
            for index in range(4):
                dx = j + mx[index]
                dy = i + my[index]
                if dy < 0 or dy >= h or dx < 0 or dx >= w:
                    return timeCount
                else :
                    if not visited2[dy][dx] and matrix[dy][dx] == '.':
                        visited2[dy][dx] = 1
                        q.append((dy,dx))
    return "IMPOSSIBLE"

T = int(input().rstrip())
mx = [1,-1,0,0]
my = [0,0,1,-1]
for loop in range(T):
    w,h = map(int,input().split())
    matrix = [list(input().rstrip()) for _ in range(h)]
    fire = []
    start = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '*':
                fire.append((i,j))
            elif matrix[i][j] == '@':
                start = (i,j)
    print(bfs())