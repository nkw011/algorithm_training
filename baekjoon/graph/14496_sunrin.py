import sys,heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        cost, node = heapq.heappop(q)
        if not visited[node]:
            visited[node] = 1
            for nxt, dist in graph[node]:
                distance[nxt] = min(distance[nxt],cost+dist)
                heapq.heappush(q,(distance[nxt],nxt))

a,b = map(int,input().split())
n,m = map(int,input().split())
visited = [0] * (n+1)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v,w = map(int,input().split())
    graph[v].append((w,1))
    graph[w].append((v,1))

dijkstra(a)
if distance[b] == INF:
    print(-1)
else:
    print(distance[b])