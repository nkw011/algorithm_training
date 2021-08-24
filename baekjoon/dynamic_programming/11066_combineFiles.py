import sys
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e8)

def combineFiles(i,j):
    global result
    if i == j : return page[i]
    if dp[i][j] != -1: return dp[i][j]
    dp[i][j] = INF
    for k in range(i,j):
        dp[i][j] = min(dp[i][j],combineFiles(i,k)+combineFiles(k+1,j))
    result += dp[i][j]
    return dp[i][j]

T = int(input())
for _ in range(T):
    n = int(input())
    page = list(map(int,input().split()))
    dp = [[-1] * n for _ in range(n)]
    matrix = [[0,0] * n for _ in range(n)]
    combineFiles(0,n-1)