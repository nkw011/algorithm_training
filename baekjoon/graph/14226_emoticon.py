import sys
input = sys.stdin.readline
from collections import deque
import heapq

n = int(input().rstrip())
visited = [[0] * 1001 for _ in range(1001)]

def bfs():
    minValue = int(1e5)
    q = []
    heapq.heappush(q,(0,0,0,1))
    
    while q:
        result,c,v,now = heapq.heappop(q)
        
        if result > minValue:
            continue
            
        if now == n:
            minValue = min(minValue,result)
            continue
            
        if now + v <= 1000 and not visited[now+v]:
            visited[now+v] = 1
            q.append((result+1,c,v,now+v))
            
        if now + c <= 1000 and not visited[now+c]:
            visited[now+c] = 1
            q.append((result+1,c,c,now+c))
            
        if now >= 1 and not visited[now-1]:
            visited[now-1] = 1
            q.append((result+1,c,v,now-1))
            
        q.append((result+1,now,v,now))
        
    return minValue

def bfs2():
    minValue = int(1e4)
    q = []
    heapq.heappush(q,(0,0,1))
    
    while q:
        result,clip,disp = heapq.heappop(q)
        
        if result > minValue:
            continue
        if disp == n:
            minValue = min(minValue,result)
            continue
        
        if disp + clip <= 1000 and not visited[disp+clip][clip]:
            visited[disp+clip][clip] = 1
            heapq.heappush(q,(result+1,clip,disp+clip))
            
        if disp -1 >=0 and not visited[disp-1][clip]:
            visited[disp-1][clip] = 1
            heapq.heappush(q,(result+1,clip,disp-1))
        if not visited[disp][disp]:
            visited[disp][disp] = 1
            heapq.heappush(q,(result+1,disp,disp))
        
    return minValue

print(bfs2())