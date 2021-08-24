import sys, heapq
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
                distance[nxt] = min(distance[nxt],dist+cost)
                heapq.heappush(q,(distance[nxt],nxt))


v,e = map(int,input().split())
start = int(input().rstrip())
graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)
distance = [INF] *(v+1)

for _ in range(e):
    a, b, cost = map(int,input().split())
    graph[a].append((b,cost))
    
dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])