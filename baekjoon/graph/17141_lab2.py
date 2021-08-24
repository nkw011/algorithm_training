import sys
input = sys.stdin.readline
from collections import deque
import itertools

def bfs(case):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    now = remain
    maxCount = 0
    for i,j in case:
        q.append((i,j,0))
        visited[i][j] = 1
    while q:
        i,j,count = q.popleft()
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy < n and 0<= dx < n:
                if not visited[dy][dx] and matrix[dy][dx] != 1:
                    maxCount = max(count+1,maxCount)
                    now -= 1
                    visited[dy][dx] = 1 
                    q.append((dy,dx,count+1))
    if now == 0 :
        return maxCount
    else :
        return n**2 + 1

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
virus = []
remain = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            virus.append((i,j))
        elif matrix[i][j] == 0:
            remain += 1
cases = list(itertools.combinations(virus,m))
mx = [1,-1,0,0]
my = [0,0,1,-1]
minResult = n**2 + 1
remain += (len(virus)-m)
for case in cases:
    minResult = min(minResult,bfs(case))
if minResult == (n**2 +1):
    print(-1)
else :
    print(minResult)