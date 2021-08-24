import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque


def bfs():
    q = deque()
    visited[n] = 1
    q.append((n,0))
    result = 0
    while q:
        num,count = q.popleft()
        if num == count:
            if count <= t:
                return count
            break
        if n+1 <= 99999 and not visited[n+1]:
            visited[n+1] = 1
            q.append((n+1,count+1))
        if n >0 and 2* n <= 99999:
            div = 1
            while div < 2*n:
                div *= 10
            div //= 10
            if not visited[2*n-div]:
                visited[2*n-div]
                q.append((2*n-div,count+1))
    return "ANG"

n,t,g = map(int,input().split())
visited = [0] * 100000
print(bfs())