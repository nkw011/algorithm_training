
# 한 번에 여러 숫자를 출력할려고 하지말고 나눠서 출력할 수 있으면 나눠서 출력하면된다.
# 이거 고민하느라 1시간 날렸네...

import sys
def input(): return sys.stdin.readline().rstrip()


def dfs(now, index):
    if now == index:
        return 1
    if dp[now][index] != -1:
        return dp[now][index]
    dp[now][index] = 0
    for nxt, cost in graph[now]:
        dp[now][index] += (cost * dfs(nxt, index))
    return dp[now][index]


n = int(input())
m = int(input())

connected = [[0] * (n+1) for _ in range(n+1)]
dp = [[-1] * (n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
basic = [1] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    basic[a] = 0
    graph[a].append((b, c))

for i in range(1, n):
    if basic[i]:
        print(i, dfs(n, i))
