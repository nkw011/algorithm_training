# dijkstra를 사용할 시 edge가 3^100000이라서 시간초과가 나온다.
# 따라서 dp를 이용했는데 pypy3를 사용하면 메모리초과가 나와서 python3로 했더니 통과하였다.

import sys
INF = int(1e8)
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(200000)


def move(loc, tgt):
    if loc == 0:
        return 2
    elif abs(tgt-loc) == 2:

        return 4
    else:
        return 3


def dfs(i, l, r):
    if i == leng-1:
        return 0
    if dp[i] != -1:
        return dp[i]
    dp[i] = INF
    if l == seq[i] or r == seq[i]:
        dp[i] = 1+dfs(i+1, l, r)
    else:
        dp[i] = min(dp[i], move(
            l, seq[i]) + dfs(i+1, seq[i], r), move(r, seq[i]) + dfs(i+1, l, seq[i]))
    return dp[i]


seq = list(map(int, input().split()))
leng = len(seq)
dp = [-1] * (leng)
print(dfs(0, 0, 0))
