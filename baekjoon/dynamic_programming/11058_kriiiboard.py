import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp=[0] * (n+1)

for i in range(1,n+1):
    dp[i] = max(dp[i],dp[i-1] +1)
    if i- 3 >= 0 :
        for j in range(i-3,0,-1):
            dp[i] = max(dp[i],dp[j] * (i-j-1))

print(dp[n])