import sys
input = sys.stdin.readline
import heapq
INF = int(1e10)

def dijkstra(start,end):
    global visited, distances
    visited = [0] * (n+1)
    distances = [INF] * (n+1)
    distances[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q :
        dist,w = heapq.heappop(q)
        if w == end:
            return dist
        if not visited[w]:
            visited[w] = 1
            for nxt,cost in graph[w]:
                distances[nxt] = min(distances[nxt],dist+cost)
                heapq.heappush(q,(distances[nxt],nxt))
    return -1

# 양방향이라 다 될 줄 알았는데 2가지로 분류하고 해야하나보네... 크흠... 아아아아아

def pResult():
    node = [1,v1,v2,n]
    node2 = [1,v2,v1,n]
    result = 0
    result2 = 0
    for i in range(3):
        number = dijkstra(node[i],node[i+1])
        number2 = dijkstra(node2[i],node2[i+1])
        if number == -1:
            result = INF
        else :
            result += number
        if number2 == -1:
            result2 = INF
        else :
            result2 += number2
    if result == INF and result2 == INF:
        return -1
    else :
        return min(result,result2)

n,e = map(int,input().split())
visited = [0] * (n+1)
distances = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1,v2 = map(int,input().split())

print(pResult())