# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

my = [1,-1,0,0]
mx = [0,0,1,-1]

def solution(maps):
    n,m = len(maps),len(maps[0])
    q = deque()
    visited = [[0] * m for _ in range(n)]
    q.append((0,0))
    visited[0][0] = 1
    while q:
        y,x = q.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x]
        for i in range(4):
            dy,dx = y + my[i], x+ mx[i]
            if 0 <= dy < n and 0 <= dx < m and maps[dy][dx] and not visited[dy][dx]:
                visited[dy][dx] = visited[y][x] + 1
                q.append((dy,dx))
    return -1
