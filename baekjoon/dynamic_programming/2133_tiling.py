# 짝수 차례마다 새로운 형태의 타일이 등장한다...
# 이걸 고려하지 않은 것 같았다.

import sys
input = sys.stdin.readline 

n = int(input().rstrip())
dp = [0,0,3,0,11]

for i in range(5,n+1):
    dp.append(dp[i-2] * 3)
    for j in range(i-2,2,-1):
        if j % 2 == 0:
            dp[i] += dp[i-j] * 2
    if i % 2 == 0:
        dp[i] += 2

print(dp[n])