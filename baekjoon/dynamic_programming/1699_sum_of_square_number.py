import sys
input = sys.stdin.readline
INF = int(1e9)

# 32 = 16 + 16 -> 2가 답이다.

n = int(input().rstrip())
dp = [INF] * (n+1)
dp[0] = 0
nxtNum = 1
for i in range(1,n+1):
    if i == (nxtNum**2):
        nxtNum += 1
    for j in range(1,nxtNum+1):
        remain = i - ((j-1)**2)
        dp[i] = min(dp[i],1+dp[remain])
print(dp[n])