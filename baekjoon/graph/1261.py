import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def bfs(i, j):
    dp[i][j] = 0
    q = deque()
    q.append((i, j))
    while q:
        y, x = q.popleft()
        for idx in range(4):
            dy, dx = y+my[idx], x+mx[idx]
            if 0 <= dy < n and 0 <= dx < m:
                if dp[dy][dx] > dp[y][x] + matrix[dy][dx]:
                    dp[dy][dx] = dp[y][x] + matrix[dy][dx]
                    q.append((dy, dx))


m, n = map(int, input().split())
dp = [[1e10] * m for _ in range(n)]
matrix = [list(map(int, input())) for _ in range(n)]
my, mx = [1, -1, 0, 0], [0, 0, 1, -1]

bfs(0, 0)

print(dp[n-1][m-1])
