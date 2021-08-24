# 그렇네 이건 LIS 문제이다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
loc = []
for _ in range(n):
    loc.append(tuple(map(int,input().split())))
loc.sort(key=lambda x:x[0])
dp = [0] * n
dp[0] = 1
for i in range(1,n):
    for j in range(i):
        if loc[i][0] > loc[j][0] and loc[i][1] > loc[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
    if dp[i] == 0:
        dp[i] = 1
print(n - max(dp))