import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visited[s] = 1
    q = deque()
    q.append((s,0))
    while q:
        num,count = q.popleft()
        if num == g:
            return count
        if num + u <= f and not visited[num+u]:
            visited[num+u] = 1
            q.append((num+u,count+1))
        if num - d >= 1 and not visited[num-d]:
            visited[num-d] = 1
            q.append((num-d,count+1))
    return -1

f,s,g,u,d = map(int,input().split())
visited = [0] * (f+1)
result = bfs()
if result != -1:
    print(result)
else :
    print("use the stairs")