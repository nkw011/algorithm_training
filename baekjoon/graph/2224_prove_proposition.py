# i!=j를 count를 셀 때 추가해야하는 이유 (반례)
# 2
# A => A
# A => B
# 2 (answer:1)
# A => B
# 1개가 나와야하는데 2개가 나오기 때문이다
# 이것 때문에 계속 틀렸다고 나왔었다... (문제를 끝까지 잘 읽자)

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
matrix = [[INF] * 52 for _ in range(52)]

for _ in range(n):
    a,b,c = input().split()
    indexA,indexC = 0,0
    if 'A' <= a <= 'Z':
        indexA = ord(a) - 65
    else :
        indexA = ord(a) - 97 + 26
    if 'A' <= c <= 'Z':
        indexC = ord(c) - 65
    else :
        indexC = ord(c) - 97 + 26
    matrix[indexA][indexC] = 1

for k in range(52):
    for i in range(52):
        for j in range(52):
            matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
            
count = 0
for i in range(52):
    for j in range(52):
        if i != j and matrix[i][j] != INF:
            count += 1

print(count)
for i in range(52):
    for j in range(52):
        if i != j and matrix[i][j] != INF :
            if 0 <= i <= 25:
                print(chr(65+i),end=" ")
            else :
                print(chr(71+i),end=" ")
            print("=>",end=" ")
            if 0 <= j <= 25:
                print(chr(65+j))
            else :
                print(chr(71+j))