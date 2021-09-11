# 각 노선을 노드로 만든 이후 역과 노선을 연결하는 그래프를 만든 다음
# 노선을 이동할 때는 이동 거리 +1 증가 역 간 이동에는 이동거리 증가를 하지 않는 방법으로 최단거리를 측정하였다.

import sys
import heapq
INF = int(1e11)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(s):
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        d, w = heapq.heappop(q)
        if dist[w] < d:
            continue
        if w == e:
            return dist[w]
        for nxt in graph[w]:
            if nxt > n:
                if dist[nxt] > d+1:
                    dist[nxt] = d+1
                    heapq.heappush(q, (d+1, nxt))
            else:
                if dist[nxt] > d:
                    dist[nxt] = d
                    heapq.heappush(q, (d, nxt))
    return -1


n, l = map(int, input().split())
graph = [[] for _ in range(n+1+l)]
for i in range(1, l+1):
    line = list(map(int, input().split()))
    for node in line:
        if node == -1:
            continue
        graph[node].append(n+i)
        graph[n+i].append(node)

s, e = map(int, input().split())

dist = [INF] * (n+l+1)
r = dijkstra(s)
if r == -1:
    print(r)
else:
    # start와 end가 같을 때 0이 아니라 -1이 출력되는 오류가 나타났다.
    if r == 0:
        print(r)
    else:
        print(r-1)
