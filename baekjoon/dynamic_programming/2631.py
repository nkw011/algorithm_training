# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-2631
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-2631/

import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
nums = [int(input()) for _ in range(n)]
dp = [0] * n
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i],dp[j])
    dp[i] += 1
print(n - max(dp))
