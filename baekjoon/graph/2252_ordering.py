import sys
input = lambda : sys.stdin.readline().rstrip()

def dfs(here):
    visited[here] =1
    for nxt in graph[here]:
        if not visited[nxt]:
            dfs(nxt)
    order.append(here)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    
order = []
visited = [0] * (n+1)
for node in range(1,n+1):
    if not visited[node]:
        dfs(node)

for i in range(n-1,-1,-1):
    print(order[i],end=" ")
print()