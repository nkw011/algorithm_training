import sys
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
loc = [list(map(int,input().split())) for _ in range(m)]

for i in range(n):
    for j in range(1,n):
        matrix[i][j] += matrix[i][j-1]
        
for array in loc:
    maxi, mini = max(array[0],array[2]), min(array[0],array[2])
    maxj, minj = max(array[1],array[3]), min(array[1],array[3])
    result = 0
    for i in range(mini-1,maxi):
        result += matrix[i][maxj-1]
        if minj-2 >= 0:
            result -= matrix[i][minj-2]
    print(result)