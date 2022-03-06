import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def bfs(s):
    visited[s] = 1
    q = deque()
    q.append(s)

    while q:
        w = q.popleft()
        for nxt in graph[w]:
            if not visited[nxt]:
                visited[nxt] = visited[w] + 1
                q.append(nxt)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

max_dist = max(visited)
node = min([i for i, d in enumerate(visited) if d == max_dist])
cnt = visited.count(max_dist)
print(node, max_dist-1, cnt)
