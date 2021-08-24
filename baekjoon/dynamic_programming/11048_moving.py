import sys
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
move = [(1,0),(0,1),(1,1)]
dp = [ array[:] for array in matrix]

for i in range(n):
    for j in range(m):
        for x,y in move:
            dx = x + j
            dy = y + i
            if 0 <= dy < n and 0 <= dx < m :
                dp[dy][dx] = max(dp[dy][dx],dp[i][j] + matrix[dy][dx])
                
print(dp[n-1][m-1])