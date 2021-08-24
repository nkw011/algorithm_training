import sys
input = lambda : sys.stdin.readline().rstrip()
INF = int(3e9)

def minMultiMatrix(i,j):
    if i== j : return 0
    if dp[i][j] != -1 : return dp[i][j]
    dp[i][j] = INF
    for k in range(i,j):
        dp[i][j] = min(dp[i][j],minMultiMatrix(i,k)+minMultiMatrix(k+1,j)+matrix[i][0] * matrix[k][1] * matrix[j][1])
    return dp[i][j]


n = int(input())
matrix = []
for i in range(n):
    a,b = map(int,input().split())
    matrix.append((a,b))
dp = [[-1] * n for _ in range(n)]
print(minMultiMatrix(0,n-1))