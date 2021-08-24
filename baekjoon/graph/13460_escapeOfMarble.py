# 남의 코드를 보고 이렇게 많이 배운건 처음이다.
# BFS 확실히 많이 공부해야겠다.
# 특히 이동에 관해 많이 배우게 되었다. // 일직선 상에서 이동하는 방법도 배웠다.
# 마지막에 visited로 방문 체크한것도 너무 좋았다.

# 실패 조건을 만들 때 실패가 다 조건에 의해 빗겨나가는 지 확인해야한다.
# 방법: 직접 조건에 not을 붙여본다.

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def move(i, j, idx):
    y, x, d = i, j, 0
    dy = my[idx]
    dx = mx[idx]
    # while 조건문의 활용
    while matrix[y+dy][x+dx] != '#' and matrix[y][x] != 'O':
        y += dy
        x += dx
        d += 1
    return (y, x, d)


def bfs(ry, rx, by, bx):
    visited[ry][rx][by][bx] = 1
    q = deque()
    q.append((ry, rx, by, bx, 0))
    while q:
        y1, x1, y2, x2, cnt = q.popleft()
        if cnt >= 10:
            continue
        for idx in range(4):
            r1, c1, d1 = move(y1, x1, idx)
            r2, c2, d2 = move(y2, x2, idx)
            if matrix[r2][c2] != 'O':
                if matrix[r1][c1] == 'O':
                    return cnt+1
                if r1 == r2 and c1 == c2:
                    if d1 < d2:
                        r2 -= my[idx]
                        c2 -= mx[idx]
                    else:
                        r1 -= my[idx]
                        c1 -= mx[idx]
                if not visited[r1][c1][r2][c2]:
                    visited[r1][c1][r2][c2] = 1
                    q.append((r1, c1, r2, c2, cnt+1))
    return -1


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]
visited = [[[[0] * m for _ in range(n)] for _ in range(m)]for _ in range(n)]

ry, rx, by, bx = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            matrix[i][j] = '.'
            ry, rx = i, j
        elif matrix[i][j] == 'B':
            matrix[i][j] = '.'
            by, bx = i, j

print(bfs(ry, rx, by, bx))
