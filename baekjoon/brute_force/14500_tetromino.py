import sys
input = sys.stdin.readline
import itertools

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

moveX = [1,-1,0,0]
moveY = [0,0,1,-1]
maxValue = 0

def dfs(matrix,count,i,j,result):
    global maxValue
    if count == 4:
        maxValue = max(maxValue,result)
        return
    
    for index in range(4):
        dx = moveX[index] + j
        dy = moveY[index] + i
        if 0<= dx < m and 0<= dy < n:
            if not visited[dy][dx]:
                visited[dy][dx] = 1
                dfs(matrix,count+1,dy,dx,result+matrix[dy][dx])
                visited[dy][dx] = 0

                
# 키보드 모양 고려 안 함
# 이런 식으로 전체 구상하는 것도 나쁘지는 않았다.
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(matrix,1,i,j,matrix[i][j])
        visited[i][j] = 0
        
# 키보드 모양 고려
move = [(1,0),(-1,0),(0,1),(0,-1)]
result = list(itertools.combinations(move,r=3))
for i in range(n):
    for j in range(m):
        for direct in result:
            Possible = True
            number = matrix[i][j]
            for x,y in direct:
                dx = j + x
                dy = i + y
                if not (0 <= dy < n) or not (0<= dx <m):
                    Possible = False
                    break
                else :
                    number += matrix[dy][dx]
            if Possible:
                maxValue = max(maxValue,number)

print(maxValue)