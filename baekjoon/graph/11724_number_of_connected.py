from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph):
    global count
    q = deque()
    for v in range(1,n+1):
        if not visited[v]:
            count += 1
            visited[v] = 1
            q.append(v)
            while q:
                w = q.popleft()
                for nxt in graph[w]:
                    if not visited[nxt]:
                        visited[nxt] = 1
                        q.append(nxt)


n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
count = 0
bfs(graph)
print(count)