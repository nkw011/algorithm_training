from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
matrix = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
move = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(matrix):
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        i,j = q.popleft()
        for x, y in move:
            dx = x + j
            dy = y + i
            if 0 <= dx < m and 0<= dy < n:
                # 방문 처리하는 게 핵심이니까 절대 까먹지 말고 하자
                if matrix[dy][dx] != 0 and not visited[dy][dx]:
                    visited[dy][dx] = 1
                    matrix[dy][dx] = matrix[i][j] + 1
                    q.append((dy,dx))
                    # 여기서 잘못 입력하는 바람에 오래걸렸네...
                    if dy == n-1 and dx == m-1 :
                        return
                    
bfs(matrix)
print(matrix[n-1][m-1])