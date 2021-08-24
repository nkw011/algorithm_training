import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def bfs():
    visited[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0, 0, 0))
    while q:
        y, x, day, cnt, reload = q.popleft()
        if y == n-1 and x == m-1:
            return day
        for idx in range(4):
            dy = y + my[idx]
            dx = x + mx[idx]
            if 0 <= dy < n and 0 <= dx < m:
                if maps[dy][dx] == 1:
                    if day % 2 == 0:
                        if cnt + 1 <= k and not visited[dy][dx][cnt+1]:
                            visited[dy][dx][cnt+1] = 1
                            q.append((dy, dx, day+1, cnt+1, 0))
                else:
                    # 이 부분에서 실수를 너무 많이 하였다.
                    if not visited[dy][dx][cnt]:
                        visited[dy][dx][cnt] = 1
                        q.append((dy, dx, day+1, cnt, 0))
        if reload < 1:
            q.append((y, x, day+1, cnt, reload+1))
    return -1


n, m, k = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]

# 출력 조건도 제대로 이해하지 못하였다.
r = bfs()
if r == -1:
    print(r)
else:
    print(r+1)
