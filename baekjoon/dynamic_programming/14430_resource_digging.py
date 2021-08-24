import sys
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = []
for array in matrix:
    dp.append(array[:])

for i in range(n):
    for j in range(m):
        if i-1 >= 0:
            dp[i][j] = max(dp[i][j],dp[i-1][j]+matrix[i][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j],dp[i][j-1]+matrix[i][j])
            
print(dp[n-1][m-1])