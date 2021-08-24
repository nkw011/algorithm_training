import sys
input = lambda : sys.stdin.readline()
from collections import deque

def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        w = q.popleft()
        for nxt in graph[w]:
            if not visited[nxt]:
                outdegree[start] += 1
                indegree[nxt] += 1
                visited[nxt] = 1
                q.append(nxt)

n,m = map(int,input().split())
result = 0
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    
indegree = [0] * (n+1)
outdegree = [0] * (n+1)

for i in range(1,n+1):
    visited =[0] * (n+1)
    bfs(i)
    
for i in range(1,n+1):
    if indegree[i] + outdegree[i] == n-1:
        result += 1
        
print(result)