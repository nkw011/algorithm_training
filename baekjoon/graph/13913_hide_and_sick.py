import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())
visited = [0] * 100001
before = [0] * 100001


def bfs():
    q = deque()
    q.append((0,n))
    visited[n] = 1
    while q :
        count, direc = q.popleft()
        
        if direc == k:
            path = []
            print(count)
            while direc != n:
                path.append(direc)
                direc = before[direc]
            print(n,end=" ")
            while path:
                print(path.pop(),end=" ")
            print()
            return
        
        if direc +1 <= 100000 and not visited[direc+1]:
            visited[direc+1] = 1
            q.append((count+1,direc+1))
            before[direc+1] = direc
        if direc -1 >= 0 and not visited[direc-1] :
            visited[direc-1] = 1
            q.append((count+1,direc-1))
            before[direc-1] = direc
        if (direc *2) <= 100000 and not visited[direc*2] :
            visited[direc*2] = 1
            q.append((count+1,direc*2))
            before[direc*2] = direc
        
bfs()