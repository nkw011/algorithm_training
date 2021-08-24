import sys
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]
temp = [[0] * n for _ in range(n)]

maxValue = 0
def calculate(temp):
    global maxValue
    for array in temp:
        first = array[0]
        count = 1
        for i in range(1,n):
            if array[i] != first:
                first = array[i]
                maxValue = max(count,maxValue)
                count = 1
            else :
                count += 1
        maxValue = max(count,maxValue)
            
    for j in range(n):
        first = temp[0][j]
        count = 1
        for i in range(1,n):
            if temp[i][j] != first:
                first = temp[i][j]
                maxValue = max(count,maxValue)
                count = 1
            else :
                count += 1
        maxValue = max(count,maxValue)

def findMaxValue():
    global n
    temp = [array[:] for array in matrix]
    
    for i in range(n):
        for j in range(n-1):
            temp[i][j], temp[i][j+1] = temp[i][j+1], temp[i][j]
            calculate(temp)
            temp = [array[:] for array in matrix]
            
    for j in range(n):
        for i in range(n-1):
            temp[i][j], temp[i+1][j] = temp[i+1][j], temp[i][j]
            calculate(temp)
            temp = [array[:] for array in matrix]
            
findMaxValue()
print(maxValue)