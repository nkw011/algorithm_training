import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)

def bfs():
    global a,b
    q = deque()
    visited = set()
    visited.add(a)
    q.append((a,0))
    while q:
        num,count = q.popleft()
        if num == b :
            return count+1
        if 1 <= num * 2<= INF and (num*2) not in visited:
            visited.add(num*2)
            q.append((num*2,count+1))
        if 1 <= num * 10 + 1 <= INF and (num*10 +1) not in visited:
            visited.add(num*10+1)
            q.append((num*10+1,count+1))
    return -1


a,b = map(int,input().split())
print(bfs())