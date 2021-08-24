import sys
input = sys.stdin.readline

move1 = [(-1,0),(0,1),(0,-1)]
move2 = [(-2,0),(-2,1),(-2,-1)]

T = int(input().rstrip())
for loop in range(T):
    n = int(input().rstrip())
    matrix = [list(map(int,input().split())) for _ in range(2)]
    dp = [array[:] for array in matrix]
    for j in range(n):
        for i in range(2):
            for x,y in move2:
                dx = x+ j
                dy = i + y
                if 0 <= dx < n and 0 <= dy < 2:
                    dp[i][j] = max(dp[i][j],dp[dy][dx] + matrix[i][j])
            if i == 0 and j-1 >= 0:
                dp[i][j] = max(dp[i][j],dp[1][j-1] + matrix[i][j])
            elif i == 1 and j-1 >= 0:
                dp[i][j] = max(dp[i][j],dp[0][j-1] + matrix[i][j])
    print(max(dp[0][n-1],dp[1][n-1]))