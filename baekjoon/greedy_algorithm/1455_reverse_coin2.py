import sys
input = sys.stdin.readline

def reverse(a,b):
    for i in range(a+1):
        for j in range(b+1):
            if matrix[i][j] == '1':
                matrix[i][j] = '0'
            else :
                matrix[i][j] = '1'

n, m = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(n)]
numOnes = [[0]*m for _ in range(n)]
number = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '1':
            number += 1
            
count = 0
while number != 0:
    maxNum = 0
    select = (0,0)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                numOnes[i][j] += 1
                if i-1 >= 0:
                    numOnes[i][j]+= numOnes[i-1][j]
                if j-1 >= 0:
                    numOnes[i][j]+= numOnes[i][j-1]
                if maxNum < numOnes[i][j]:
                    maxNum = numOnes[i][j]
                    select = (i,j)
                
    if maxNum > 0:
        count += 1
        number -= maxNum
        number += ((select[0]+1) * (select[1]+1) - maxNum)
        numOnes = [[0]*m for _ in range(n)]
        reverse(select[0],select[1])
print(count)