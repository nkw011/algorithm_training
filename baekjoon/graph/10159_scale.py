n = int(input())
m = int(input())
matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    matrix[a][b] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            matrix[i][j] = matrix[i][j] or ( matrix[i][k] and matrix[k][j])
            
for i in range(1,n+1):
    matrix[i][i] = 1

for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if matrix[i][j] or matrix[j][i]:
            continue
        count +=1
    print(count)