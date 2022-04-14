# 풀이 및 해설: https://nkw011.github.io/baekjoon/baekjoon-2229/

import sys
def input(): return sys.stdin.readline().rstrip()
n = int(input())
scores = list(map(int,input().split()))
# diff[i][j]: scores[j:i+1]의 최댓값과 최솟값의 차이
diff = [[0] * n for _ in range(n)]
for i in range(n):
    max_n, min_n = -1,1e10
    for j in range(i,-1,-1):
        if max_n < scores[j]: max_n = scores[j]
        if min_n > scores[j]: min_n = scores[j]
        diff[i][j] = max_n - min_n
        
dp = [0] * n
max_n, min_n = -1,1e10
for i in range(n):
    if scores[i] > max_n: max_n = scores[i]
    if scores[i] < min_n: min_n = scores[i]
    dp[i] = max_n - min_n
    for j in range(i):
        if dp[i] < dp[j] + diff[i][j+1]:
            dp[i] = dp[j] + diff[i][j+1]
print(dp[n-1])
