# 비트마스킹을 활용한 BFS 문제였다.
# 생각이 잘 맞아서 다행이었다.

import sys
from collections import deque
from typing import Type
def input(): return sys.stdin.readline().rstrip()


def convert(c):
    if 'A' <= c <= 'F':
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a')


def bfs(sy, sx):
    visited[sy][sx][0] = 1
    q = deque()
    q.append((sy, sx, 0, 0))
    while q:
        y, x, key, cnt = q.popleft()
        for idx in range(4):
            dy = y + my[idx]
            dx = x + mx[idx]
            if 0 <= dy < n and 0 <= dx < m:
                if visited[dy][dx][key] or matrix[dy][dx] == '#':
                    continue
                visited[dy][dx][key] = 1
                if 'a' <= matrix[dy][dx] <= 'f':
                    q.append(
                        (dy, dx, key | (1 << convert(matrix[dy][dx])), cnt+1))
                elif 'A' <= matrix[dy][dx] <= 'F':
                    if key & (1 << convert(matrix[dy][dx])):
                        q.append((dy, dx, key, cnt+1))
                elif matrix[dy][dx] == '1':
                    return cnt + 1
                else:
                    q.append((dy, dx, key, cnt+1))
    return -1


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[[0] * (2 << 6) for _ in range(m)] for _ in range(n)]
my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]


start = -1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '0':
            start = (i, j)
            break

print(bfs(start[0], start[1]))
