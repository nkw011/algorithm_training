# 첫번째 틀린 이유: a에 대해 bfs를 돌 때 b를 visited 처리하지 않았음
# 두번째 틀린 이유: a먼저 b나중만 하고 b먼저 a나중을 하지 않아서 틀렸다.

# 기본적인 bfs 문제여서 기초를 다지는 아주 중요한 문제가 되었다.

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def bfs(start, target, visited, parent):
    y1, x1 = start[1], start[0]
    y2, x2 = target[1], target[0]

    visited[y1][x1] = 1
    q = deque()
    q.append((y1, x1))

    while q:
        y, x = q.popleft()
        if y == y2 and x == x2:
            return

        for idx in range(4):
            dy = y + my[idx]
            dx = x + mx[idx]
            if 0 <= dy < (m+1) and 0 <= dx < (n+1):
                if not visited[dy][dx]:
                    visited[dy][dx] = visited[y][x] + 1
                    parent[dy][dx] = [y, x]
                    q.append((dy, dx))
    return


def findResult(f1, f2, l1, l2):
    visited1 = [[0] * (n+1) for _ in range(m+1)]
    visited2 = [[0] * (n+1) for _ in range(m+1)]
    parent = [[[0, 0] for _ in range(n+1)] for _ in range(m+1)]

    visited1[l1[1]][l1[0]] = 1
    visited1[l2[1]][l2[0]] = 1

    bfs(f1, f2, visited1, parent)
    r1 = visited1[f2[1]][f2[0]] - 1

    y, x = f2[1], f2[0]
    while not (y == f1[1] and x == f1[0]):
        visited2[y][x] = 1
        y, x = parent[y][x][0], parent[y][x][1]
    visited2[y][x] = 1

    bfs(l1, l2, visited2, parent)
    r2 = visited2[l2[1]][l2[0]] - 1

    if r1 == -1 or r2 == -1:
        return "IMPOSSIBLE"
    else:
        return r1+r2


n, m = map(int, input().split())
loc = [tuple(map(int, input().split())) for _ in range(4)]

my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]

r1 = findResult(loc[0], loc[1], loc[2], loc[3])
r2 = findResult(loc[2], loc[3], loc[0], loc[1])

if r1 == "IMPOSSIBLE" and r2 == "IMPOSSIBLE":
    print(r1)
else:
    if r1 == "IMPOSSIBLE":
        print(r2)
    elif r2 == "IMPOSSIBLE":
        print(r1)
    else:
        print(min(r1, r2))
