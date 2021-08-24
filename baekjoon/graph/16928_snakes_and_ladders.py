import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
matrix = [0] * 101
visited = [0] * 101
ladders = [0] * 101
snakes = [0] * 101
for _ in range(n):
    a,b = map(int,input().split())
    matrix[a] = 1
    ladders[a] = b
for _ in range(m):
    a,b = map(int,input().split())
    matrix[a] = 2
    snakes[a] = b
    
def bfs():
    q = deque()
    q.append((1,0))
    visited[1] = 1
    while q:
        now,count = q.popleft()
        if now == 100:
            return count
        if not matrix[now]:
            for num in range(6,0,-1):
                if now + num <= 100 and not visited[now+num]:
                    visited[now+num] = 1
                    q.append((now+num,count+1))
        else :
            if matrix[now] == 1 and not visited[ladders[now]]:
                visited[ladders[now]] = 1
                q.append((ladders[now],count))
            elif matrix[now] == 2 and not visited[snakes[now]]:
                visited[snakes[now]] = 1
                q.append((snakes[now],count))

print(bfs())