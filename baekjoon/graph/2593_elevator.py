# 이전에 배운 걸 복습할 수 있는 좋은 기회였다.
# 기억해낸 것이 다행이었다.

import sys
import heapq
INF = int(1e10)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(s):
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        cnt, w = heapq.heappop(q)
        if dist[w] < cnt:
            continue
        if w == e:
            return cnt
        for nxt in graph[w]:
            if nxt >= n+1:
                if dist[nxt] > cnt+1:
                    dist[nxt] = cnt+1
                    heapq.heappush(q, (dist[nxt], nxt))
                    parent[nxt] = w
            else:
                if dist[nxt] > cnt:
                    parent[nxt] = w
                    dist[nxt] = cnt
                    heapq.heappush(q, (dist[nxt], nxt))
    return -1


n, m = map(int, input().split())
graph = [[] for _ in range(n+m+1)]
parent = [0] * (n+m+1)
dist = [INF] * (n+m+1)

for i in range(1, m+1):
    x, y = map(int, input().split())
    for floor in range(x, n+1, y):
        graph[n+i].append(floor)
        graph[floor].append(n+i)

s, e = map(int, input().split())

r = dijkstra(s)
print(r)
if r != -1:
    v = e
    ele = []
    cnt = 0
    while v != s:
        if v >= n+1:
            ele.append(v-n)
            cnt += 1
        v = parent[v]
    for i in range(cnt-1, -1, -1):
        print(ele[i])
