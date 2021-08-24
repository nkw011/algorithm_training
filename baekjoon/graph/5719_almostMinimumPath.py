# 그래프 시작 노드가 1이라고 착각했었다.
# 실제로 시작은 0부터 시작한다. (이것때문에 10번 틀렸다...)
# 문제 똑바로 읽자


import sys
import heapq
from collections import deque
INF = int(1e10)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(s):
    dist[s] = 0
    q = []
    heapq.heappush(q, (dist[s], s))
    while q:
        d, w = heapq.heappop(q)
        if dist[w] < d:
            continue
        # 그래프 시작 노드가 1이라고 착각했었다.
        # 실제로 시작은 0부터 시작한다. (이것때문에 10번 틀렸다...)
        for nxt in range(n+1):
            if edge[w][nxt] == -1:
                continue
            if dist[nxt] > d + edge[w][nxt]:
                dist[nxt] = d + edge[w][nxt]
                heapq.heappush(q, (dist[nxt], nxt))
                parent[nxt].clear()
                parent[nxt].add(w)
            elif dist[nxt] == d + edge[w][nxt]:
                parent[nxt].add(w)


def removeEdge(e):
    q = deque()
    q.append(e)
    while q:
        x = q.popleft()
        for before in parent[x]:
            if dist[before] + edge[before][x] == dist[x]:
                edge[before][x] = -1
                q.append(before)


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    s, e = map(int, input().split())
    dist = [INF] * (n+1)
    edge = [[-1] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        edge[u][v] = p
    parent = [set() for _ in range(n+1)]
    dijkstra(s)
    removeEdge(e)
    dist = [INF] * (n+1)
    dijkstra(s)
    if dist[e] != INF:
        print(dist[e])
    else:
        print(-1)
