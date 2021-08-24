# 상한선을 잘 설정해야하다는 것을 알게된 문제이다.
# 최단거리에서 상한선 즉, 제일 아래가 되는 부분들을 잘 설정하자


import sys
import heapq
INF = int(1e18)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(s):
    q = []
    dist[s][0] = 0
    heapq.heappush(q, (0, s, 0))
    while q:
        d, w, count = heapq.heappop(q)
        if d > dist[w][count]:
            continue
        for nxt, c in graph[w]:
            if d + c < dist[nxt][count]:
                dist[nxt][count] = d+c
                heapq.heappush(q, (dist[nxt][count], nxt, count))
            if count < k and d < dist[nxt][count+1]:
                dist[nxt][count+1] = d
                heapq.heappush(q, (dist[nxt][count+1], nxt, count+1))


n, m, k = map(int, input().split())
dist = [[INF] * (k+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)

result = INF
for t in dist[n]:
    result = min(result, t)
print(result)
