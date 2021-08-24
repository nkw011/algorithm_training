# 이건 그냥 파이썬이라서 시간초과가 계속 나오는 것 같다.

import sys
import heapq
INF = int(1e8)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s, 0))
    while q:
        hour, here, price = heapq.heappop(q)
        if cache[here][price] < hour:
            continue
        for nxt, c, d in graph[here]:
            if price + c > m:
                continue
            if cache[nxt][price+c] < hour + d:
                continue

            for j in range(price+c, m+1):
                if cache[nxt][j] > hour + d:
                    cache[nxt][j] = hour + d
            heapq.heappush(q, (hour+d, nxt, price+c))
    result = INF
    for t in cache[n]:
        result = min(result, t)
    if result == INF:
        print("Poor KCM")
    else:
        print(result)


T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    cache = [[INF] * (m+1) for _ in range(n+1)]
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    dijkstra(1)
