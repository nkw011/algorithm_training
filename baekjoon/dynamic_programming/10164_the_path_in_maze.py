import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][1] = 1
if k == 0:
    for i in range(1,n+1):
        for j in range(1,m+1):
            if dp[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
else :
    r = k // m if k % m != 0 else k//m-1
    c = k - (r*m) if k % m != 0 else m
    for i in range(1,r+2):
        for j in range(1,c+1):
            if dp[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    for i in range(r+1,n+1):
        for j in range(c,m+1):
            if dp[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
print(dp[n][m])