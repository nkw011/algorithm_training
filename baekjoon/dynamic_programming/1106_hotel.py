# c의 최댓값이 1000이기 때문에
# 1000보다 더 많이 반복문이 돌아야한다.

import sys
input = sys.stdin.readline

c,n = map(int,input().split())
dp = [0] *(2001)
city = []
for _ in range(n):
    a,b = map(int,input().split())
    city.append((a,b))
    
for i in range(1,2001):
    minCost = int(1e9)
    for cost,num in city:
        if i >= num:
            minCost = min(minCost,dp[i-num] + cost)
    dp[i] = minCost
    
print(min(dp[c:]))