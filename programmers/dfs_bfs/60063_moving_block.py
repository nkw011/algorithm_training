# 해설: https://velog.io/@nkw011/programmers-60063

from collections import deque

my = [1,-1,0,0]
mx = [0,0,1,-1]

def solution(board):
    N = len(board)
    visited = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    visited[0][0][0] = 1
    visited[0][1][0] = 1
    q = deque([(0,0,0,1,0,0)])
    while q:
        y1,x1,y2,x2,cnt, direc = q.popleft()
        if (y1, x1) == (N - 1, N - 1) or (y2, x2) == (N - 1, N - 1):
            return cnt

        for i in range(4):
            dy1,dx1,dy2,dx2 = y1 + my[i], x1 + mx[i], y2 + my[i], x2 + mx[i]
            if not (0 <= dy1 < N and 0 <= dx1 < N and 0 <= dy2 < N and 0 <= dx2 < N): continue
            if board[dy1][dx1] or board[dy2][dx2]: continue
            if (visited[dy1][dx1][direc] and visited[dy2][dx2][direc]): continue

            visited[dy1][dx1][direc] = 1
            visited[dy2][dx2][direc] = 1
            q.append((dy1, dx1, dy2, dx2, cnt + 1, direc))

        if direc == 0:
            for ny1,nx1,ny2,nx2 in [(y1,x1,y2,x2),(y2,x2,y1,x1)]:
                for i in [1,-1]:
                    if ny1 - i < 0 or ny1 - i >= N: continue
                    if board[ny2-i][nx2] or board[ny1-i][nx1] or visited[ny1-i][nx1][1]: continue

                    visited[ny1-i][nx1][1] = 1
                    visited[ny1][nx1][1] =1
                    if ny1-i > ny1:
                        q.append((ny1,nx1,ny1-i,nx1,cnt+1,1))
                    else:
                        q.append((ny1-i,nx1,ny1,nx1,cnt+1,1))
        else:
            for ny1, nx1, ny2, nx2 in [(y1, x1, y2, x2), (y2, x2, y1, x1)]:
                for i in [1, -1]:
                    if nx1 - i < 0 or nx1 - i >= N: continue
                    if board[ny2][nx2-i] or board[ny1][nx1-i] or visited[ny1][nx1-i][0]: continue

                    visited[ny1][nx1-i][0] = 1
                    visited[ny1][nx1-i][0] = 1
                    if nx1 - i > nx1:
                        q.append((ny1, nx1, ny1, nx1-i, cnt + 1, 0))
                    else:
                        q.append((ny1, nx1-i, ny1, nx1, cnt + 1, 0))
    return -1


################# 처음 풀이 #################

def solution(board):
    N = len(board)
    visited = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    visited[0][0][0] = 1
    visited[0][1][0] = 1
    q = deque([(0,0,0,1,0,0)])
    while q:
        y1,x1,y2,x2,cnt, direc = q.popleft()
        if (y1, x1) == (N - 1, N - 1) or (y2, x2) == (N - 1, N - 1):
            return cnt
        for i in range(4):
            dy1,dx1,dy2,dx2 = y1 + my[i], x1 + mx[i], y2 + my[i], x2 + mx[i]
            if 0 <= dy1 < N and 0 <= dx1 < N and 0 <= dy2 < N and 0 <= dx2 < N:
                if not board[dy1][dx1] and not board[dy2][dx2]:
                    if not (visited[dy1][dx1][direc] and visited[dy2][dx2][direc]):
                        visited[dy1][dx1][direc] = 1
                        visited[dy2][dx2][direc] = 1
                        q.append((dy1,dx1,dy2,dx2,cnt+1,direc))
        if direc == 0:
            if y2 -1 >= 0 and y1 -1 >= 0:
                if not board[y2-1][x2] and not board[y1-1][x1] and not visited[y1-1][x1][1]:
                    visited[y1 - 1][x1][1] = 1
                    visited[y1][x1][1] = 1
                    q.append((y1,x1,y1-1,x1,cnt+1,1))
                if not board[y1-1][x1] and not board[y2-1][x2] and not visited[y2-1][x2][1]:
                    visited[y2 - 1][x2][1] = 1
                    visited[y2][x2][1] = 1
                    q.append((y2-1,x2,y2,x2,cnt+1,1))
            if y2 +1 < N and y1 + 1 < N:
                if not board[y2+1][x2] and not board[y1+1][x1] and not visited[y1+1][x1][1]:
                    visited[y1+ 1][x1][1] = 1
                    visited[y1][x1][1] = 1
                    q.append((y1,x1,y1+1,x1,cnt+1,1))
                if not board[y1+1][x1] and not board[y2+1][x2] and not visited[y2+1][x2][1]:
                    visited[y2 + 1][x2][1] = 1
                    visited[y2][x2][1] = 1
                    q.append((y2,x2,y2+1,x2, cnt+1,1))
        if direc == 1:
            if x1 -1 >= 0 and x2 -1 >= 0:
                if not board[y2][x2-1] and not board[y1][x1-1] and not visited[y1][x1-1][0]:
                    visited[y1][x1-1][0] = 1
                    visited[y1][x1][0] = 1
                    q.append((y1,x1-1,y1,x1,cnt+1,0))
                if not board[y1][x1-1] and not board[y2][x2-1] and not visited[y2][x2-1][0]:
                    visited[y2][x2-1][0] = 1
                    visited[y2][x2][0] = 1
                    q.append((y2,x2-1,y2,x2,cnt+1,0))
            if x1 + 1 < N  and x2+1 < N:
                if not board[y2][x2+1] and not board[y1][x1+1] and not visited[y1][x1+1][0]:
                    visited[y1][x1+1][0] = 1
                    visited[y1][x1][0] = 1
                    q.append((y1,x1,y1,x1+1,cnt+1,0))
                if not board[y1][x1+1] and not board[y2][x2+1] and not visited[y2][x2+1][0]:
                    visited[y2][x2+1][0] = 1
                    visited[y2][x2][0] = 1
                    q.append((y2,x2,y2,x2+1,cnt+1,0))
    return -1

if __name__ == '__main__':
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    print(solution(board))
