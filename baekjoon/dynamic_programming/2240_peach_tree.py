import sys
input = sys.stdin.readline
input = lambda : sys.stdin.readline().rstrip()

t,w = map(int,input().split())
tree = [int(input().rstrip()) for _ in range(t)]
dp = [[0] * (w+1) for _ in range(t+1)]
for i in range(1,t+1):
    for j in range(w+1):
        ts = 1 if j% 2 == 0 else 2
        if j == 0:
            if ts == tree[i-1]:
                dp[i][j] = dp[i-1][j] + 1
            else :
                dp[i][j] = dp[i-1][j]
        else :
            if ts == tree[i-1]:
                dp[i][j] = max(dp[i][j],dp[i-1][j]+1,dp[i-1][j-1] +1)
            else :
                dp[i][j] = max(dp[i][j],dp[i-1][j],dp[i-1][j-1])
                
print(max(dp[t]))