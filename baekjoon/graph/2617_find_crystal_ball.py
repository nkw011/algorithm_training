# 보니까 union-find로도 풀 수 있는 것 같긴하다. (부모를 자기보다 큰 것으로 생각하던지 / 작은 것으로 생각하던지 해서)

import sys
input = sys.stdin.readline
INF = int(1e5)

n,m = map(int,input().split())
matrix = [[INF] * (n+1) for _ in range(n+1)]
matrix2 = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    matrix[s][e] = 1
    matrix2[e][s] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
            matrix2[i][j] = min(matrix2[i][j],matrix2[i][k]+matrix2[k][j])
result = set()            
for i in range(1,n+1):
    count = 0
    count2 = 0
    for j in range(1,n+1):
        if matrix[i][j] != INF:
            count += 1
        if matrix2[i][j] != INF:
            count2 += 1
    if count >= ((n+1) //2) or count2 >= ((n+1) //2):
        result.add(i)
        
print(len(result))