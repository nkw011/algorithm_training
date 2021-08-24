import sys
input = lambda : sys.stdin.readline().rstrip()

def countTime(order):
    if dp[order] != -1 : return dp[order]
    dp[order] = 0
    for nxt in graph[order]:
        dp[order] = max(dp[order],countTime(nxt))
    dp[order] += delay[order]
    return dp[order]


n = int(input())
delay = [0] * n 
graph = [[] for _ in range(n)]
dp = [-1] * n
for i in range(n):
    work = list(map(int,input().split()))
    delay[i] = work[0]
    for nxt in work[2:]:
        graph[i].append(nxt-1)
result = 0
for order in range(n):
    result = max(result,countTime(order))
print(result)