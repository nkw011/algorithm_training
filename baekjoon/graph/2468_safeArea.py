from collections import deque
import sys
input = sys.stdin.readline

move = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(matrix):
    global maxValue
    temp = [[0] * n for _ in range(n)]
    maxCount = 0
    visited = []
    q = deque()
    # maxValue가 1일 수도 있기 때문에 maxValue -1을 하면 안된다.
    for number in range(maxValue):
        count = 0
        visited = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                temp[i][j] = matrix[i][j] - number
        
        for i in range(n):
            for j in range(n):
                if temp[i][j] > 0 and not visited[i][j]:
                    count += 1
                    visited[i][j] = 1
                    q.append((i,j))
                    while q:
                        r,c = q.popleft()
                        for x,y in move:
                            dx = x + c
                            dy = y + r
                            if 0 <= dx < n and 0 <= dy < n:
                                if temp[dy][dx] > 0 and not visited[dy][dx]:
                                    visited[dy][dx] = 1
                                    q.append((dy,dx))
        maxCount = max(maxCount,count)
    return maxCount


n = int(input().rstrip())
matrix = [list(map(int,input().split())) for _ in range(n)]
maxValue = 0
for i in range(n):
    for j in range(n):
        if maxValue < matrix[i][j]:
            maxValue = matrix[i][j]
print(bfs(matrix))