import sys
input = sys.stdin.readline

def combination(n,m):
    if n == m or m == 0 :
        return 1
    if m == 1:
        return n
    
    if dp[n][m] != 0:
        return dp[n][m]
    
    dp[n][m] = combination(n-1,m) + combination(n-1,m-1)
    return dp[n][m]

n,m = map(int,input().split())
dp = [[0]* (n+1) for _ in range(n+1)]

print(combination(n,m))