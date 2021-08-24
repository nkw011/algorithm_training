import sys
import heapq
INF = int(1e13)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(s, dist, check):
    q = []
    dist[s] = 0
    heapq.heappush(q, (dist[s], s))
    while q:
        d, w = heapq.heappop(q)
        if dist[w] < d:
            continue
        if check[w]:
            continue
        check[w] = 1
        for nxt, c in graph[w]:
            if not check[nxt] and height[nxt-1] > height[w-1] and dist[nxt] > d+c:
                dist[nxt] = d+c
                heapq.heappush(q, (dist[nxt], nxt))


n, m, d, e = map(int, input().split())
height = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
dist1 = [INF] * (n+1)
dist2 = [INF] * (n+1)
check1 = [0] * (n+1)
check2 = [0] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1, dist1, check1)
dijkstra(n, dist2, check2)

result = -INF
for i in range(1, n+1):
    if dist1[i] == INF or dist2[i] == INF:
        continue
    result = max(result, (height[i-1] * e) - (dist1[i]+dist2[i])*d)

if result == -INF:
    print("Impossible")
else:
    print(result)
