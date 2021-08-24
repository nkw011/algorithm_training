# 리뷰1
# 일단 먼저 문제를 꼼꼼히 읽지 못해서 발생하는 문제에 대해 1시간 정도 낭비하였다.(제일 주의해야하는부분)
# 두번째로, 무리해서 계산을 하는 버릇이 있어서 사이즈가 작은 것에 대해서는 정상작동하였지만
# 사이즈가 크면 정상작동되지 않았다.(한 번에 여러개를 계산하는 것보다 하나씩 도출해서 계산하는 것이 좋음)
# 세번째로 이미 물고기를 먹은 칸에서 한 번 더 탐색 과정이 이루어지기때문에 발생하는 시간 지연이 한 몫했다.

# BFS가 최단거리를 보장해주기는 하지만 특정조건이 있는 최단거리는 만족을 보장해주지는 못한다.
# 따라서 특정조건이 있는 것은 최단거리에 해당하는 모든 것을 찾은 이후 특정 조건을 만족하는 단 하나의 값을 리턴하는 것이 좋다.

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global shark, size, result,remain,sizeCount
    q = deque()
    visited = [[0] * n for _ in range(n)]
    matrix[shark[0]][shark[1]] = 0
    visited[shark[0]][shark[1]] = 1
    q.append((shark[0],shark[1],0))
    eat =[]
    while q:
        i,j,count = q.popleft()
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0<= dy < n and 0<= dx < n:
                if not visited[dy][dx]:
                    if 0 < matrix[dy][dx] < size:
                        visited[dy][dx] = 1
                        eat.append((dy,dx,count+1))
                    elif 0 <= matrix[dy][dx] <= size:
                        visited[dy][dx] = 1
                        q.append((dy,dx,count+1))
    eat.sort(key=lambda x:(x[2],x[0],x[1]))
    if len(eat) > 0:
        return eat[0]
    return -1,-1,-1

n = int(input().rstrip())
matrix = [list(map(int,input().split())) for _ in range(n)]
fish = [0] * 7
shark = (0,0)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            shark = (i,j)
        elif 0 < matrix[i][j] < 7:
            fish[matrix[i][j]] += 1

mx = [1,-1,0,0]
my = [0,0,1,-1]
size = 2
sizeCount = 0
result = 0
remain = fish[1]
while remain > 0:
    x,y,count = bfs()
    if x == -1 and y == -1:
        break
    matrix[x][y] = 0
    result += count
    shark = (x,y)
    sizeCount += 1
    remain -= 1
    if sizeCount == size:
        if size < 7:
            remain += fish[size]
        size += 1
        sizeCount = 0
print(result)