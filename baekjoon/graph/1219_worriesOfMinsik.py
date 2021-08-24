# 전형적인 벨만포드 알고리즘 문제이다.


import sys
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)
M = int(1e8)

def bellmanFord(start):
    upper[start] = 0
    for it in range(n-1):
        updated = False
        for v in range(n):
            for nxt,cost in graph[v]:
                if upper[nxt] > upper[v] + cost:
                    upper[nxt] = upper[v] + cost
                    updated = True
        if not updated:
            break
    for v in range(n):
        for nxt,cost in graph[v]:
            if upper[nxt] > upper[v] + cost:
                if connected[start][v] and connected[v][end]:
                    return -1
    return 1



n,start,end,m = map(int,input().split())
graph = [[] for _ in range(n)]
connected = [[0] * n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c*(-1)))
    connected[a][b] = 1
    
    
profit = list(map(int,input().split()))
for adj in graph :
    leng = len(adj)
    for i in range(leng):
        adj[i] = (adj[i][0],adj[i][1] + profit[adj[i][0]])
        adj[i] = (adj[i][0],adj[i][1] * -1)

upper = [INF] * n
visited = [0] * n

for k in range(n):
    for i in range(n):
        for j in range(n):
            connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])
            
            
ret = bellmanFord(start)
if ret == -1: print('Gee')
else :
    if upper[end] >= INF - M:
        print('gg')
    else :
        print(upper[end] * (-1) + profit[start])