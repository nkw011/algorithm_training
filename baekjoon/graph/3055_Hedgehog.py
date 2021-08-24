import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(n)]
visited1 = [[0] * m for _ in range(n)]
visited2 = [[0] * m for _ in range(n)]

water = []
animal = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '*':
            water.append((i,j))
            visited1[i][j] = 1
        elif matrix[i][j] == 'S':
            animal.append((i,j))
            visited2[i][j] = 1
            
moveX = [1,-1,0,0]
moveY = [0,0,1,-1]

def bfs():
    global water, animal
    count = 0
    while animal :
        q1 = deque(water)
        q2 = deque(animal)
        water = []
        while q1:
            r,c = q1.popleft()
            for index in range(4):
                dx = c + moveX[index]
                dy = r + moveY[index]
                if 0 <= dy < n and 0 <= dx < m:
                    if not visited1[dy][dx] and matrix[dy][dx] == '.':
                        visited1[dy][dx] = 1
                        matrix[dy][dx] = '*'
                        water.append((dy,dx))
        if len(animal) != 0:
            count += 1
        animal = []
        while q2:
            r,c = q2.popleft()
            for index in range(4):
                dx = c + moveX[index]
                dy = r + moveY[index]
                if 0 <= dy < n and 0 <= dx < m:
                    if matrix[dy][dx] == 'D':
                        return count
                    if not visited2[dy][dx] and matrix[dy][dx] == '.':
                        visited2[dy][dx] = 1
                        animal.append((dy,dx))
    return "KAKTUS"

print(bfs())