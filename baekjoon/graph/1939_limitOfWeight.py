import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
INF = 1000000000

def bfs(s):
    global mid,t
    visited[s] = 1
    q = deque()
    q.append(s)
    while q:
        w = q.popleft()
        if w == t: return True
        for nxt,cost in graph[w]:
            if not visited[nxt] and cost >= mid:
                visited[nxt] =1
                q.append(nxt)
    return False

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append(((a,c)))
s,t = map(int,input().split())
visited = [0] * (n+1)
    
left = 1
right = INF
result = 1
while left <= right:
    mid = (left+right) //2
    visited = [0] * (n+1)
    if bfs(s):
        left = mid+1
        result = max(result,mid)
    else :
        right = mid -1
print(result)