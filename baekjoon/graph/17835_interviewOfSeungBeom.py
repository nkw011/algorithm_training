# 투표소 -> 도시방향으로 가장 먼 위치에 있는 도시를 찾는 것이기 때문에 다익스트라를 이용했다.
# 투표소 -> 도시방향이기 때문에 도로 방향을 반대로 만ㄷ르어서 진행하였다.
# 핵심: 마지막으로 k개마다 다익스트라를 돌리면 시간초과가 나오기 때문에 임의의 지점에서 투표소로 가는 도로를 만들고 cost를 0으로 설정해
# 임의의 지점에서 모든 도시까지의 거리 중 최장 거리를 구하는 방식으로 진행하였다.

import sys
import heapq
INF = int(1e11)
def input(): return sys.stdin.readline().rstrip()


def findLongest():
    q = []
    for i in candi:
        dist[i] = 0
        heapq.heappush(q, (0, i))
    while q:
        d, w = heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt, cost in graph[w]:
            if dist[nxt] > d+cost:
                dist[nxt] = d+cost
                heapq.heappush(q, (d+cost, nxt))


n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))

dist = [INF] * (n+1)
candi = list(map(int, input().split()))

findLongest()
v = 0
for i in range(1, n+1):
    if v == 0 or dist[v] < dist[i]:
        v = i
print(v)
print(dist[v])
