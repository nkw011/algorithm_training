import sys
input = sys.stdin.readline
import heapq
from collections import deque

n,k = map(int,input().split())
visited = [0] * 100001

def bfs():
    global minValue
    q = []
    heapq.heappush(q,(0,n))
    while q :
        count, direc = heapq.heappop(q)
        visited[direc] = 1
        if direc == k:
            print(count)
            return
        if direc +1 <= 100000 and not visited[direc+1]:
            heapq.heappush(q,(count+1,direc+1))
        if direc -1 >= 0 and not visited[direc-1] :
            heapq.heappush(q,(count+1,direc-1))
        if (direc *2) <= 100000 and not visited[direc*2] :
            heapq.heappush(q,(count,direc*2))
        
bfs()