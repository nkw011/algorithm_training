import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def bfs(i, j):
    q = deque()
    visited[i][j] = 1
    q.append((i, j))
    cnt = 1
    while q:
        r, c = q.popleft()
        for idx in range(4):
            dy, dx = r + my[idx], c + mx[idx]
            if 0 <= dy < m and 0 <= dx < n:
                if not visited[dy][dx] and matrix[dy][dx] == matrix[i][j]:
                    visited[dy][dx] = 1
                    cnt += 1
                    q.append((dy, dx))
    return cnt


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]

W, B = 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            count = bfs(i, j)
            if matrix[i][j] == 'W':
                W += (count**2)
            else:
                B += (count**2)
print(W, B)
