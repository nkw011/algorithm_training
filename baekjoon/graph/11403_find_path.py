import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
distance = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if distance[i][j] == 0:
            distance[i][j] = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i][j] = min(distance[i][j],distance[i][k] + distance[k][j])
            
for i in range(n):
    for j in range(n):
        if distance[i][j] != INF:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()