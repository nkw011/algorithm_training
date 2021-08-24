from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph,start):
    global count
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        w = q.popleft()
        for nxt in graph[w]:
            if not visited[nxt]:
                count += 1
                visited[nxt] = 1
                q.append(nxt)


n = int(input().rstrip())
m = int(input().rstrip())
graph =[[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    
count = 0
bfs(graph,1)
print(count)