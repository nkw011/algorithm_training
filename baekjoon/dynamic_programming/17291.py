import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0] * (n+1)
dp[1] = 1
for i in range(2,n+1):
    dp[i] = 2 * dp[i-1]
    if i % 2 == 0:
        if i >= 4:
            dp[i] -= dp[i-3]
        if i >= 5:
            dp[i] += dp[i-4]
        if i >= 6:
            dp[i] -= dp[i-5]
print(dp[n])