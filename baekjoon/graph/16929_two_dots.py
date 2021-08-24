# 일단 keeping해놓고 다른 문제 푼 다음에 다시 풀어야겠다.
# DFS로 풀고 4번 예시가 왜 cycle인지 확인해보기 (확인함)
# DFS로 사이클 순환하는 방법 기억하기

import sys
input = sys.stdin.readline

mx = [1,-1,0,0]
my = [0,0,1,-1]

def dfs(i,j,count,before):
    global isCycle
    if isCycle:
        return
    
    for index in range(4):
        dx = j + mx[index]
        dy = i + my[index]
        if 0 <= dy < n and 0 <= dx < m:
            if matrix[dy][dx] == matrix[i][j]:
                if count >= 4 and visited[dy][dx] and (dy,dx) != before:
                    isCycle = True
                    return
                if not visited[dy][dx]:
                    visited[dy][dx] = 1
                    dfs(dy,dx,count+1,(i,j))
                    visited[dy][dx] = 0

n,m  = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
isCycle = False

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,(50,50))
        visited[i][j] = 0
        if isCycle:
            break
    if isCycle:
        break
if isCycle:
    print("Yes")
else :
    print("No")
    
# def cycle(i,j,row,col):
#     isEnd = True
#     count = 1
#     if row == INF:
#         for r in range(i,n):
#             if matrix[r][j] != matrix[i][j]:
#                 if r-1 >= 0:
#                     row = r-1
#                     isEnd = False
#                     break
#         if isEnd:
#             row = n-1
#         if row == i:
#             return False
#         count += (row-i)
#     if col == INF:
#         isEnd = True
#         for c in range(j,m):
#             if matrix[i][c] != matrix[i][j]:
#                 if c-1 >= 0:
#                     isEnd = False
#                     col = c-1
#                     count += c-1-j
#                     break
#         if isEnd:
#             col = m-1
#         if col == j:
#             return False
#         count += (col-j)
#     if matrix[row][col] != matrix[i][j]:
#         return False
#     for c in range(j,col+1):
#         if matrix[row][c] != matrix[i][j]:
#             return False
#         count +=1
#     for r in range(i,row+1):
#         if matrix[r][col] != matrix[i][j]:
#             return False
#         count += 1
#     if count < 4:
#         return False
#     return True