# 과연 다른 사람들은 어떻게 풀었을까?
# 아주 좋은 풀이를 많이보고 배우게 되었다. -> 위상정렬과 역추적경로를 활용한 풀이


import sys
import heapq
INF = int(1e10)
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(100000)


def dijkstra(s):
    dist[s] = 0
    q = []
    heapq.heappush(q, (dist[s], s))
    while q:
        d, w = heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt, c in graph[w]:
            if dist[nxt] > d+c:
                dist[nxt] = d+c
                parent[nxt].clear()
                parent[nxt].add(w)
                heapq.heappush(q, (d+c, nxt))
            elif dist[nxt] == d+c:
                parent[nxt].add(w)


# 이 부분이 아마 시간을 제일 많이 잡아 먹고 있는 것 같다.
def countEdge(d):
    visited[d] = 1
    ret = 0
    for nxt in parent[d]:
        if not visited[nxt]:
            ret += (1+countEdge(nxt))
        else:
            ret += 1
    return ret


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
parent = [set() for _ in range(n+1)]
visited = [0] * (n+1)
dist = [INF] * (n+1)
dp = [-1] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, -c))
s, e = map(int, input().split())
dijkstra(s)
result = countEdge(e)
print(dist[e] * (-1))
print(result)
