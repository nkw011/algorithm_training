# 가장 긴 부분 수열이 아닌 가장 큰 부분 수열이다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
inputs = list(map(int,input().split()))
dp = [0] * n
for i in range(n):
    for j in range(i):
        if inputs[i] > inputs[j]:
            dp[i] = max(dp[i],dp[j] + inputs[i])
    if dp[i] == 0:
        dp[i] = inputs[j]
        
print(max(dp))