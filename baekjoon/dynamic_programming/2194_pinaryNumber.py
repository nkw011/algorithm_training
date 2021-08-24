import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp =[[0,1],[1,0],[1,1]]

for i in range(3,n):
    dp.append([0,0])
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[n-1]))