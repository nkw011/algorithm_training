import sys
input = sys.stdin.readline
INF = int(1e9)

def printMatrix(matrix,length):
    for i in range(1,length+1):
        for j in range(1,length+1):
            if matrix[i][j] == INF:
                print("INF",end=" ")
            else:
                print(matrix[i][j],end=" ")
        print()


n = int(input().rstrip())
matrix = [[INF] *(n+1) for _ in range(n+1)]
while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    matrix[a][b] = 1
    matrix[b][a] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            # 플로이드-와샬 알고리즘에서 같은 인덱스끼리의 거리는 0이다. -> 이 부분을 꼭 기억해두자
            if i == j:
                continue
            matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])

result = []
minResult = INF
for i in range(1,n+1):
    maxCount = 0
    for j in range(1,n+1):
        if matrix[i][j] != INF and matrix[i][j] > maxCount:
            maxCount = matrix[i][j]
    minResult = min(maxCount,minResult)
    result.append(maxCount)

count = 0
for num in result:
    if num == minResult:
        count += 1

print(minResult,count)
for i in range(n):
    if result[i] == minResult: print(i+1,end=" ")
print()