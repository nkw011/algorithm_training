import sys
import heapq
from collections import deque
INF = int(1e11)
def input(): return sys.stdin.readline().rstrip()


def findSafe():
    queue = deque()
    visited = [0] * (n+1)
    for c in zombie:
        visited[c] = 1
        queue.append(c)
    while queue:
        w = queue.popleft()
        for nxt in graph[w]:
            if not visited[nxt]:
                visited[nxt] = visited[w] + 1
                queue.append(nxt)
    for i in range(1, n+1):
        if 0 < visited[i]-1 <= s:
            charge[i] = q
        elif visited[i]-1 > s or visited[i] == 0:
            charge[i] = p


def dijkstra():
    path = []
    dist[1] = 0
    heapq.heappush(path, (dist[1], 1))
    while path:
        c, w = heapq.heappop(path)
        if dist[w] < c:
            continue
        if w == n:
            return c
        for nxt in graph[w]:
            if not charge[nxt]:
                continue
            if dist[nxt] > c + charge[nxt]:
                dist[nxt] = c + charge[nxt]
                heapq.heappush(path, (dist[nxt], nxt))


n, m, k, s = map(int, input().split())
p, q = map(int, input().split())

zombie = [int(input()) for _ in range(k)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

charge = [0] * (n+1)
dist = [INF] * (n+1)

findSafe()
print(dijkstra()-charge[n])
