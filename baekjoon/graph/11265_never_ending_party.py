import sys
input = sys.stdin.readline
INF = int(1e10)

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])

for _ in range(m):
    a,b,c = map(int,input().split())
    if matrix[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")