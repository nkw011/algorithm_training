# 나머지 계산을 한다는 것에 항상 주의하자

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0] = [1] * (k+1)
dp[1] = [i for i in range(k+1)]

for i in range(2,n+1):
    for num in range(1,k+1):
        for j in range(i+1):
            dp[i][num] += dp[i-j][num-1]
            dp[i][num] %= 1000000000
            
print(dp[n][k])