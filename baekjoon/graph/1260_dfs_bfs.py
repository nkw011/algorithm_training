import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)
for _ in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    
for array in graph:
    array.sort()
    
def dfs(graph,node):
    if not visited2[node]:
        visited2[node] = 1
        print(node,end=" ")
        for nxt in graph[node]:
            dfs(graph,nxt)
        return
    return

def dfs2(graph,start):
    stack1 = deque()
    stack1.append(start)
    while stack1:
        v = stack1.pop()
        if not visited2[v]:
            visited2[v] = 1
            print(v,end=" ")
            stack1.append(v)
            nxt = 0
            for w in graph[v]:
                if not visited2[w]:
                    nxt = w
                    break
            while nxt:
                print(nxt,end=" ")
                visited2[nxt] = 1
                stack1.append(nxt)
                changed = False
                for w in graph[nxt]:
                    if not visited2[w]:
                        changed = True
                        nxt = w
                        break
                if not changed:
                    nxt = 0

def bfs(graph,start):
    q = deque()
    q.append(start)
    while q:
        w = q.popleft()
        if not visited1[w]:
            print(w,end=" ")
            visited1[w] = 1
            for nxt in graph[w]:
                q.append(nxt)
                
dfs(graph,v)
print()
bfs(graph,v)