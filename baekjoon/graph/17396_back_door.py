import heapq
import sys
input = sys.stdin.readline
INF = int(3e11)

def dijkstra(start):
    distances[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, w = heapq.heappop(q)
        if not visited[w]:
            visited[w] = 1
            for nxt,cost in graph[w]:
                if not enemys[nxt] or (enemys[nxt] and nxt == n-1):
                    distances[nxt] = min(distances[nxt],dist+cost)
                    heapq.heappush(q,(distances[nxt],nxt))
    if distances[n-1] != INF :
        print(distances[n-1])
    else :
        print(-1)

n,m = map(int,input().split())
enemys = list(map(int,input().split()))
graph = [[] for _ in range(n)]
distances  = [INF] * n
visited = [0] * n
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
dijkstra(0)