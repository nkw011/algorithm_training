from collections import deque
import sys
input = sys.stdin.readline

move = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(matrix):
    global n,m
    count = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                count += 1
                matrix[i][j] = count
                visited[i][j] = 1
                q.append((i,j))
                while q:
                    r,c = q.popleft()
                    for x,y in move:
                        dx = c + x
                        dy = r + y
                        if 0 <= dy < n and 0 <= dx < m:
                            if matrix[dy][dx] == 1 and not visited[dy][dx]:
                                matrix[dy][dx] = count
                                visited[dy][dx] = 1
                                q.append((dy,dx))
    return count


T = int(input().rstrip())
for _ in range(T):
    m,n,k = map(int,input().split())
    matrix = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        c,r = map(int,input().split())
        matrix[r][c] = 1
    
    print(bfs(matrix))