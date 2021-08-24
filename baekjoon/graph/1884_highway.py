# 양방향 도로가 아닌데 양방향 도로로 계산을 해서 문제를 틀렸던 것이다.
# visited[w][count]를 하면 안되었던 이유는 해당 조건(w위치에 count만큼 비용지불)을 가지고도 더 짧게 들어올 수 있기 때문이다.
# 즉, 방문체크를 하는 방식으로 하면 안되었다.

import sys
import heapq
INF = int(1e15)
def input(): return sys.stdin.readline().rstrip()


def bfs():
    dist[1][0] = 0
    q = []
    heapq.heappush(q, (0, 1, 0))
    while q:
        d, w, count = heapq.heappop(q)
        if dist[w][count] < d:
            continue
        for nxt, l, t in graph[w]:
            if count + t > k:
                continue
            if dist[nxt][count+t] > d + l:
                dist[nxt][count+t] = d+l
                heapq.heappush(q, (d+l, nxt, count+t))
    return -1


k = int(input())
n = int(input())
r = int(input())
graph = [[] for _ in range(n+1)]
dist = [[INF] * (k+1) for _ in range(n+1)]
for _ in range(r):
    s, d, l, t = map(int, input().split())
    graph[s].append((d, l, t))

bfs()

ret = INF
for i in range(k+1):
    ret = min(dist[n][i], ret)

if ret == INF:
    print(-1)
else:
    print(ret)
