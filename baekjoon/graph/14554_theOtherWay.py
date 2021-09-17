import sys
import heapq
INF = int(1e15)
MOD = 1000000009
def input(): return sys.stdin.readline().rstrip()


def dijkstra():
    q = []
    dist[s] = 0
    cnt[s] = 1
    heapq.heappush(q, (0, s))
    while q:
        d, w = heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt, c in graph[w]:
            if dist[nxt] > d+c:
                dist[nxt] = d+c
                cnt[nxt] = cnt[w]
                heapq.heappush(q, (d+c, nxt))
            elif dist[nxt] == d+c:
                cnt[nxt] += cnt[w]
                cnt[nxt] %= MOD


n, m, s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


dist = [INF] * (n+1)
cnt = [0] * (n+1)
dijkstra()
print(cnt[e])
