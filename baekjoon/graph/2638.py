# 풀이 및 해설1: https://nkw011.github.io/baekjoon/baekjoon-2638/
# 풀이 및 해설2: https://velog.io/@nkw011/baekjoon-2638

import sys
from collections import deque
from itertools import chain
def input(): return sys.stdin.readline().rstrip()

def bfs():
    empty = [(0,0), (0,m-1), (n-1,0), (n-1,m-1)]
    visited = [[0]* m for _ in range(n)]
    q = deque(empty)
    cnt = 0
    for y, x in empty:
        visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for idx in range(4):
            dy, dx = y + my[idx], x + mx[idx]
            if dy <0 or dy >= n or dx <0 or dx >= m: continue
            if matrix[dy][dx]:
                visited[dy][dx] += 1
                if visited[dy][dx] == 2:
                    matrix[dy][dx] = 0
                    cnt += 1
            if not visited[dy][dx]:
                visited[dy][dx] = 1
                q.append((dy,dx))
    return cnt

def time_count():
    cheeze_cnt = sum(chain(*matrix))
    t = 0
    while cheeze_cnt > 0:
        cheeze_cnt -= bfs()
        t += 1
    return t

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
my = [1,-1,0,0]
mx = [0,0,1,-1]

print(time_count())
