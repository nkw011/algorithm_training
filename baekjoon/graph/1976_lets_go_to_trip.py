import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
matrix = [list(map(int,input().split())) for _ in range(n)]

# 시작지점과 도착지점이 같을 수도 있다.
for i in range(n):
    matrix[i][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0 and matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

city = list(map(int,input().split()))
possible = True
for i in range(m-1):
    if not matrix[city[i]-1][city[i+1]-1]:
        print("NO")
        possible = False
        break
if possible :
    print("YES")