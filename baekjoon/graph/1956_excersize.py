import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
distances = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    distances[a][b] = c
    
for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            distances[i][j] = min(distances[i][j],distances[i][k] + distances[k][j])

result = INF
for i in range(1,v+1):
    if distances[i][i] != INF:
        result = min(result,distances[i][i])
if result == INF:
    print(-1)
else :
    print(result)