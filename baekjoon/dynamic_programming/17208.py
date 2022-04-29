# 풀이 및 해설: https://nkw011.github.io/baekjoon/baekjoon-17208/

import sys
def input(): return sys.stdin.readline().rstrip()

def solve(idx, burger,fry):
    if idx == n: return 0
    if dp[idx][burger][fry] != -1: return dp[idx][burger][fry]
    dp[idx][burger][fry] = 0
    if burger >= order_list[idx][0] and fry >= order_list[idx][1]:
        dp[idx][burger][fry] = 1 + solve(idx+1,burger - order_list[idx][0], fry - order_list[idx][1])
    dp[idx][burger][fry] = max(dp[idx][burger][fry], solve(idx+1,burger,fry))
    return dp[idx][burger][fry]


n,m,k = map(int, input().split())
order_list = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[[-1] * (k+1) for _ in range(m+1)] for _ in range(n)]

print(solve(0,m,k))
