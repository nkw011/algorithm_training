import sys
input = sys.stdin.readline

n,m = map(int,input().split())
matrixA = []
matrixB = []
count = 0

def change(matrix,i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if matrix[x][y] == '0':
                matrix[x][y] = '1'
            else :
                matrix[x][y] = '0'

for _ in range(n*2):
    if count < n :
        matrixA.append(list(input()))
        count += 1
    else:
        matrixB.append(list(input()))
        
def makeEqual():
    if n < 3 or m < 3 :
        for i in range(n):
            for j in range(m):
                if matrixA[i][j] != matrixB[i][j]:
                    return -1
        return 0

    count = 0
    for i in range(n-2):
        for j in range(m-2):
            if matrixA[i][j] != matrixB[i][j]:
                change(matrixA,i,j)
                count += 1
                
    for i in range(n):
        for j in range(m):
            if matrixA[i][j] != matrixB[i][j]:
                return -1
    return count

print(makeEqual())