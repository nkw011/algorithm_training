# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-14950
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-14950/

import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().rstrip()

def bfs():
    result, cnt = 0, 0
    visited = [0] * (n+1)
    visited[1] = 1
    q = []
    for nxt, c in graph[1]:
        heappush(q,(c,nxt))
    while q:
        cost, w = heappop(q)
        if visited[w]: continue
        visited[w] = 1
        result += cost + (cnt * t)
        cnt += 1
        for nxt, c in graph[w]:
            if not visited[nxt]:
                heappush(q,(c, nxt))
    return result

n, m, t = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

print(bfs())
