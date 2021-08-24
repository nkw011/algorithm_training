# 그리디가 최적해가 아니다...

import sys
input = sys.stdin.readline

n = int(input().rstrip())

tetra = [0] * (125)
tri = [0] * (125)
tetra[1] = 1
tri[1] = 1
index = 0
for i in range(2,125):
    tri[i] = tri[i-1] + i
    tetra[i] = tetra[i-1] + tri[i]
    if tetra[i] > n:
        index = i-1
        break
        
# 거스름돈 걸러주기 문제와 같이 그리디라고 착각하기가 쉽지만
# 그리디가 최적해가 아니다.
dp = [0] * (n+1)
for i in range(1,n+1):
    minCount = int(1e9)
    for j in range(index,0,-1):
        if i >= tetra[j]:
            minCount = min(minCount,dp[i-tetra[j]]+1)
    dp[i] = minCount
    
print(dp[n])