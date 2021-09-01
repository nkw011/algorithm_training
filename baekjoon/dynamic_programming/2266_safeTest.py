import sys
INF = int(1e11)
def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j == 1:
            dp[i][j] = i
        else:
            dp[i][j] = INF
            # 깨질 때와 깨지지 않을 때가 있다는 것!
            # 문제를 끝까지 잘 읽자!
            for floor in range(1, i+1):
                dp[i][j] = min(dp[i][j], max(
                    dp[floor-1][j-1], dp[i-floor][j])+1)

print(dp[n][k])
