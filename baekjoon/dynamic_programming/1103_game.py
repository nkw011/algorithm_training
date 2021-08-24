# 사이클이 발생하면 무한의 값이 나오기 때문에 -1을 출력해야된다.
# 따라서 사이클을 판별하기 가장 쉬운 dfs로 구현하였다.
# dp는 cross edge가 발생할 때 쓴다. 이미 방문하고 종료도 했기 때문에 사이클은 나오지 않고 계산결과도 이미 나와있다.
# 따라서 이런 결과값을 사용하기 위해 dp를 쓴다. -> 시간 절약
# 뭔가 만족스러운 문제였다.

import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(100000)


def dfs(i, j):
    global cycle
    if cycle:
        return False
    if matrix[i][j] == 'H':
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    visited[i][j] = 1
    dp[i][j] = 0
    for idx in range(4):
        dy = i + matrix[i][j] * my[idx]
        dx = j + matrix[i][j] * mx[idx]
        if 0 <= dy < n and 0 <= dx < m:
            if not visited[dy][dx]:
                dp[i][j] = max(dp[i][j], 1+dfs(dy, dx))
            else:
                if not finished[dy][dx]:
                    cycle = True
                    return -1
                else:
                    dp[i][j] = max(dp[i][j], 1+dfs(dy, dx))
        else:
            dp[i][j] = max(dp[i][j], 1)
    finished[i][j] = 1
    return dp[i][j]


n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    inputs = list(input())
    for j in range(m):
        if inputs[j] == 'H':
            matrix[i][j] = 'H'
        else:
            matrix[i][j] = int(inputs[j])

visited = [[0] * m for _ in range(n)]
finished = [[0] * m for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]

cycle = False
ret = dfs(0, 0)
if not cycle:
    print(ret)
else:
    print(-1)
