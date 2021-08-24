import sys,heapq
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e8)

def dijkstra(s):
    distance[s] = 0
    q = []
    heapq.heappush(q,(distance[s],s))
    while q:
        dist,w = heapq.heappop(q)
        if dist > distance[w] : continue
        for nxt,cost in graph[w]:
            if distance[nxt] > dist + cost:
                distance[nxt] = dist+cost
                parent[nxt] = w
                heapq.heappush(q,(distance[nxt],nxt))
    return

def dijkstra2(s):
    dist2[s] = 0
    q = []
    heapq.heappush(q,(distance[s],s))
    while q:
        dist,w = heapq.heappop(q)
        if dist > distance[w] : continue
        for nxt,cost in graph[w]:
            if not visited[nxt] and dist2[nxt] > dist + cost:
                dist2[nxt] = dist+cost
                parent[nxt] = w
                heapq.heappush(q,(dist2[nxt],nxt))
    return


def isAlreadyVisited(s):
    v = s
    while parent[v] != v:
        visited[v] = 1
        v = parent[v]
    visited[v] = 1
    return 


T = int(input())
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    distance =[INF] * (n+1)
    result = 0
    parent = [ i for i in range(n+1)]
    
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    
    target = [int(input()) for _ in range(t)]
    dijkstra(s)
    target.sort()
    
    visited = [0] * (n+1)
    dist2 = [INF] * (n+1)
    
    if distance[g] < distance[h]:
        dijkstra2(h)
        isAlreadyVisited(h)
        for tgt in target:
            if dist2[tgt] + distance[h] == distance[tgt]:
                print(tgt,end=' ')
    else :
        dijkstra2(g)
        isAlreadyVisited(g)
        for tgt in target:
            if dist2[tgt] + distance[g] == distance[tgt]:
                print(tgt,end=' ')
    print()