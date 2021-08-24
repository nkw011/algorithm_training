# 도대체 어떤 차이였을까?
# 난 잘 모르겠다... (일단 문제에서 구현하라고 하는 것은 다 구하였더니 완료함..)

import sys
import heapq
INF = int(1e15)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(s):
    dist[s] = 0
    q = []
    heapq.heappush(q, (dist[s], s))
    while q:
        d, w = heapq.heappop(q)
        if d > dist[w]:
            continue
        for nxt, c in graph[w]:
            if dist[nxt] > d+c:
                dist[nxt] = d+c
                heapq.heappush(q, (dist[nxt], nxt))


n, m = map(int, input().split())
j = int(input())
k = int(input())

tp = [0] * (n+1)
reds = list(map(int, input().split()))
blues = list(map(int, input().split()))

for red in reds:
    tp[red] = 'A'
for blue in blues:
    tp[blue] = 'B'

graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(j)

r = INF
b = INF
for red in reds:
    if dist[red] == INF:
        continue
    if r > dist[red]:
        r = dist[red]

for blue in blues:
    if dist[blue] == INF:
        continue
    if b > dist[blue]:
        b = dist[blue]

# 아마 이 부분이 잘 구현이 안되지 않았난 생각해본다.
if r == INF and b == INF:
    print(-1)
elif r <= b:
    print("A")
    print(r)
else:
    print("B")
    print(b)
