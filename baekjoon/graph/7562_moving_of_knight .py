import sys
input = sys.stdin.readline
from collections import deque

mx = [-2,-1,1,2,-2,-1,1,2]
my = [1,2,2,1,-1,-2,-2,-1]

def bfs(start,want):
    visited[start[0]][start[1]] = 1
    q = deque()
    q.append(start)
    while q:
        i,j = q.popleft()
        if i == want[0] and j == want[1]:
            return matrix[i][j]

        for index in range(8):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dx < l and 0 <= dy < l:
                if not visited[dy][dx]:
                    visited[dy][dx] = 1
                    matrix[dy][dx] = matrix[i][j] + 1
                    q.append((dy,dx))
    return -1

T = int(input().rstrip())
for loop in range(T):
    l = int(input().rstrip())
    now = tuple(map(int,input().split()))
    want = tuple(map(int,input().split()))
    matrix = [[0] * l for _ in range(l)]
    visited = [[0] * l for _ in range(l)]
    print(bfs(now,want))