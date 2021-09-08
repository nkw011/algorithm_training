# 1415. 사탕 문제를 풀기 전 워밍업 문제이다.

import sys
def input(): return sys.stdin.readline().rstrip()


def convert(i, remain):
    if i >= k:
        return remain == 0
    if dp[i][remain] != -1:
        return dp[i][remain]
    dp[i][remain] = 0
    for j in range(coin[i][1]+1):
        if remain >= coin[i][0] * j:
            dp[i][remain] += convert(i+1, remain-coin[i][0] * j)
    return dp[i][remain]


t, k = int(input()), int(input())
coin = [tuple(map(int, input().split())) for _ in range(k)]

dp = [[-1] * (t+1) for _ in range(k)]

print(convert(0, t))
