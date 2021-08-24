import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(index,start):
    distances[index][start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, w = heapq.heappop(q)
        if not visited[w]:
            for nxt,cost in graph[w]:
                visited[w] = 1
                distances[index][nxt] = min(distances[index][nxt],dist+cost)
                heapq.heappush(q,(distances[index][nxt],nxt))


T = int(input().rstrip())
for loop in range(T):
    n,m = map(int,input().split())
    graph= [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    k = int(input().rstrip())
    starts = list(map(int,input().split()))
    distances = [[INF] * (n+1) for _ in range(k)]
    visited = [0] * (n+1)
    for i in range(k):
        dijkstra(i,starts[i])
        visited = [0]* (n+1)
    result = INF
    node = n+1
    for i in range(1,n+1):
        count = 0
        for j in range(k):
            count += distances[j][i]
        if count < result:
            result = count
            node = i
        elif count == result:
            node = min(node,i)
    print(node)