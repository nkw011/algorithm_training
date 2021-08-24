import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
miro = list(map(int,input().split()))
dp = [INF] * n
dp[0] = 0
for i in range(n):
    if dp[i] != INF:
        for j in range(miro[i]+1):
            if i + j < n:
                dp[i+j] = min(dp[i+j],dp[i]+1)
if dp[n-1] == INF:
    print(-1)
else:
    print(dp[n-1])