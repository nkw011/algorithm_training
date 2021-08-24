import sys
input = lambda : sys.stdin.readline().rstrip()

def countMinTime(here):
    if dp[here] != -1 : return dp[here]
    dp[here] = 0
    for nxt in graph[here]:
        dp[here] = max(dp[here],countMinTime(nxt))
    dp[here] += delay[here]
    return dp[here]


T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    delay = list(map(int,input().split()))
    graph = [[] for _ in range(n)]
    dp = [-1] * n
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y-1].append(x-1)
    w = int(input())
    print(countMinTime(w-1))