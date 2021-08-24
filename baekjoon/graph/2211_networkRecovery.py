# 시작점이 고정되어있는 전형적인 다익스트라 알고리즘 문제이다.

import sys
import heapq
def input(): return sys.stdin.readline().rstrip()


INF = int(1e8)


def dijkstra():
    dist[1] = 0
    q = []
    heapq.heappush(q, (dist[1], 1))
    while q:
        d, w = heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt, c in graph[w]:
            if dist[nxt] > d + c:
                dist[nxt] = d+c
                parent[nxt] = w
                heapq.heappush(q, (dist[nxt], nxt))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra()

print(n-1)
for i in range(2, n+1):
    print(parent[i], i)
