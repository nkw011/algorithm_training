import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [[0] * 6 for _ in range(12)]
    possible = False
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and matrix[i][j] != '.':
                colors = [(i,j)]
                count = 1
                q = deque()
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    r,c = q.popleft()
                    for index in range(4):
                        dx = c + mx[index]
                        dy = r + my[index]
                        if 0 <= dy < 12 and 0 <= dx < 6:
                            if not visited[dy][dx] and matrix[dy][dx] == matrix[i][j]:
                                visited[dy][dx] = 1
                                colors.append((dy,dx))
                                count += 1
                                q.append((dy,dx))
                if count >= 4:
                    possible = True
                    for r,c in colors:
                        matrix[r][c] = '.'
    return possible

def gravity():
    index = 12
    change = False
    q = []
    for j in range(6):
        for i in range(11,-1,-1):
            if matrix[i][j] != '.':
                index = i
                for r in range(i+1,12):
                    if matrix[r][j] == '.':
                        index = r
                    else :
                        break
                if index != i:
                    matrix[index][j] = matrix[i][j]
                    matrix[i][j] = '.'

matrix = [list(input().rstrip()) for _ in range(12)]
mx = [1,-1,0,0]
my = [0,0,1,-1]
result = 0

while bfs():
    result += 1
    gravity()
print(result)