import sys
input = lambda : sys.stdin.readline().rstrip()

def architect(num):
    if dp[num] != -1 : return dp[num]
    dp[num] = 0
    for nxt in graph[num]:
        dp[num] = max(dp[num],architect(nxt))
    dp[num] += delay[num]
    return dp[num]


n = int(input())
delay = [0] * n
graph = [[] for _ in range(n)]
dp = [-1] * n
for i in range(n):
    work = list(map(int,input().split()))
    delay[i] = work[0]
    for nxt in work[1:]:
        if nxt == -1: break
        graph[i].append(nxt-1)
        
for i in range(n):
    print(architect(i))