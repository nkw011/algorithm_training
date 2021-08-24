# 일반적인 traveling sales person 문제이다.

import sys
INF = int(1e8)
def input(): return sys.stdin.readline().rstrip()


def tsp(here, visited):
    if visited == (1 << n) - 1:
        if not dist[here][start]:
            return INF
        return dist[here][start]
    if dp[here][visited] != -1:
        return dp[here][visited]
    dp[here][visited] = INF
    for nxt in range(n):
        if visited & (1 << nxt) or not dist[here][nxt]:
            continue
        dp[here][visited] = min(
            dp[here][visited], dist[here][nxt] + tsp(nxt, visited+(1 << nxt)))
    return dp[here][visited]


n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]
start = 0
print(tsp(0, 1))
