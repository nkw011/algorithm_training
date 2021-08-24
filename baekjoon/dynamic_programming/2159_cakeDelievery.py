import sys
INF = int(1e6)
def input(): return sys.stdin.readline().rstrip()


n = int(input())
sy, sx = map(int, input().split())
loc = [[] for _ in range(n)]

for i in range(n):
    y, x = map(int, input().split())
    loc[i].append((y, x))
    if y + 1 <= 100000:
        loc[i].append((y+1, x))
    if x + 1 <= 100000:
        loc[i].append((y, x+1))
    if y-1 >= 1:
        loc[i].append((y-1, x))
    if x-1 >= 1:
        loc[i].append((y, x-1))

dp = [[] for _ in range(n)]
dist = [INF] * n


# 같을 때랑 초과일 때랑 구분해서 해주어야한다.

for r, c in loc[0]:
    if dist[0] >= abs(sy-r) + abs(sx-c):
        dist[0] = abs(sy-r) + abs(sx-c)
        dp[0].append((r, c))

for i in range(1, n):
    for r, c in loc[i]:
        for y, x in dp[i-1]:
            if dist[i] >= abs(r-dp[i-1][0]) + abs(c-dp[i-1][1]):
                dist[i] = abs(r-dp[i-1][0]) + abs(c-dp[i-1][1])
    dist[i] += dist[i-1]
print(dist[n-1])
