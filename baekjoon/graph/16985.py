import sys
from collections import deque
from itertools import permutations
INF = 5 **3
def input(): return sys.stdin.readline().rstrip()

# 시계 (i,j) -> (j,n-1-i)
# 반시계 (i,j) -> (n-1-j,i)
# 어차피 시계 방향 4번 돌리는 것과 반시계 방향 4번 돌리는 것은 같다.
def rotate_clock(arr):
    temp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[j][4-i] = arr[i][j]
    return temp

def bfs(matrix):
    if not matrix[0][0][0]: return INF
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1 
    q = deque([(0,0,0)])
    while q:
        z,y,x = q.popleft()
        if z == 4 and y == 4 and x == 4:
            return visited[z][y][x] - 1
        for idx in range(6):
            dz,dy,dx = z + mz[idx], y + my[idx], x + mx[idx]
            if 0 <= dz < 5 and 0 <= dy < 5 and 0 <= dx < 5:
                if not visited[dz][dy][dx] and matrix[dz][dy][dx]:
                    visited[dz][dy][dx] = visited[z][y][x] + 1
                    q.append((dz,dy,dx))
    return INF

def solve(index):
    global result
    if index == 5:
        cnt = bfs(array)
        if result > cnt:
            result = cnt
        return
    for _ in range(4):
        array[index] = rotate_clock(array[index])
        solve(index + 1)


matrix = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]

mz = [1,-1,0,0,0,0]
my = [0,0,1,-1,0,0]
mx = [0,0,0,0,1,-1]

result = INF
for array in permutations(matrix):
    array = list(array)
    solve(0)
if result != INF:
    print(result)
else:
    print(-1)
