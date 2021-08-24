import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
distance = [[INF] * n for _ in range(n)]

for i in range(n):
    distance[i][i] = 0

for _ in range(m):
    a, b = map(int,input().split())
    distance[a-1][b-1] = 1
    distance[b-1][a-1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])

minValue = INF
person = n
for i in range(n):
    result = sum(distance[i])
    if result < minValue:
        minValue = result
        person = i+1
print(person)