from collections import deque
import sys
input = sys.stdin.readline

move = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

def bfs(matrix):
    count = 0
    q = deque()
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and not visited[i][j]:
                count += 1
                matrix[i][j] = count
                visited[i][j] = 1
                q.append((i,j))
                while q:
                    r,c = q.popleft()
                    for x,y in move:
                        dx = c + x
                        dy = y + r
                        if 0 <= dy < h and 0 <= dx < w:
                            if matrix[dy][dx] == 1 and not visited[dy][dx]:
                                matrix[dy][dx] = count
                                visited[dy][dx] = 1
                                q.append((dy,dx))
    return count

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    print(bfs(matrix))