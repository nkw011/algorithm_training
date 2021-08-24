import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distances[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q :
        dist, w = heapq.heappop(q)
        if not visited[w]:
            visited[w] = 1
            for nxt, cost in graph[w]:
                distances[nxt] = min(distances[nxt],dist+cost)
                heapq.heappush(q,(distances[nxt],nxt))

n,m = map(int,input().split())
visited = [0] * (n+1)
distances = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dijkstra(1)
print(distances[n])