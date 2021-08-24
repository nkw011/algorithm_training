# 양방향 그래프라도 minDistance(s,e)와 minDistance(e,s)가 다르다!!!!!!!!! 이거 중요!!1
# 두 번째로 두 로봇이 이동해야할 거리의 최솟값이므로 
# 지금 두 지점이 떨어진 거리랑 다익스트라로 구한 최솟값이 똑같으면 이동을 하지 않아도 되므로 최솟값은 0이 된다.
# start와 end가 정해지지 않았다면 둘 다 start,end 각각 해봐야한다!!!!
import sys
input = sys.stdin.readline
import heapq
INF = int(1e10)

def dijkstra(start,end):
    distances[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, w = heapq.heappop(q)
        if w == end:
            return dist
        if not visited[w]:
            visited[w] = 1
            for nxt,cost in graph[w]:
                distances[nxt] = min(distances[nxt],dist+cost)
                if not visited[nxt]:
                    nodes[nxt] = (w,cost)
                q.append((distances[nxt],nxt))


n,s,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
distances = [INF] * (n+1)
nodes = [0] * (n+1)
visited = [0] * (n+1)
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
result = dijkstra(s,e)
temp1, temp2 = s,e
if s == e:
    print(0)
else :
    maxLength = 0
    while nodes[e][0] != s:
        maxLength = max(maxLength,nodes[e][1])
        e = nodes[e][0]
    if result >= maxLength:
        result -= maxLength
    
    distances = [INF] * (n+1)
    nodes = [0] * (n+1)
    visited = [0] * (n+1)
    result2 = dijkstra(temp2,s)
    
    maxLength2 = 0
    while nodes[s][0] != temp2:
        maxLength2 = max(maxLength2,nodes[s][1])
        s = nodes[s][0]
    if result2 >= maxLength2:
        result2 -= maxLength2
    result = min(result,result2)
    for nxt,cost in graph[temp1]:
        if nxt == temp2:
            if cost == result:
                result = 0
            break
    print(result)
    