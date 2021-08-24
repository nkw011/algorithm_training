import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][0],dp[1][1] = 1,1

for i in range(2,n+1):
    for j in range(m+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
print(dp[n][m] % 10007)