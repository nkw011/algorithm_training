# 다익스트라를 다시 보고 배워야겠다는 생각이 든다.

import sys
import heapq
INF = int(1e18)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s, gas[s-1]))
    while q:
        dist, idx, cost = heapq.heappop(q)
        if check[idx][cost]:
            continue
        if idx == n:
            return dist

        check[idx][cost] = 1
        for nxt, c in graph[idx]:
            if check[nxt][min(cost, gas[nxt-1])]:
                continue
            heapq.heappush(q, (dist+c*cost, nxt, min(cost, gas[nxt-1])))
    return -1


n, m = map(int, input().split())
gas = list(map(int, input().split()))
check = [[0] * (2501) for _ in range(n+1)]
dist = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra(1))
