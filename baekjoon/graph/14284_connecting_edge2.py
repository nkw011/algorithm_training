# 연결그래프는 단방향 그래프, 양방향 그래프 모두 가리킨다.

import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    distances[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q :
        dist, w = heapq.heappop(q)
        if w == t:
            return dist
        if not visited[w]:
            visited[w] = 1
            for nxt,cost in graph[w]:
                distances[nxt] = min(distances[nxt],cost+dist)
                heapq.heappush(q,(distances[nxt],nxt))



n,m = map(int,input().split())
distances = [INF] * (n+1)
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
s,t = map(int,input().split())
print(dijkstra(s))