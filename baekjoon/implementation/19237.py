# 해설: https://nkw011.github.io/baekjoon/baekjoon-19237/

import sys
def input(): return sys.stdin.readline().rstrip()

def bfs(smell_q):
    moved = {}
    q = {}
    
    for k in range(1,m+1):
        if k not in shark: continue
        y,x,d = shark[k]
        ny,nx,nd, n_smell = 0,0,0,-1
        for move_d in shark_move[k][d]:
            dy,dx = y + my[move_d], x + mx[move_d]
            if 0 <= dy < n and 0 <= dx < n:
                if (n_smell == -1  or n_smell == 1) and not visited[dy][dx]:
                    ny,nx,nd,n_smell = dy,dx,move_d, 0
                if n_smell == -1 and visited[dy][dx] == k:
                    ny,nx,nd,n_smell = dy,dx,move_d,1
        if (ny,nx) not in moved:
            shark[k] = (ny,nx,nd)
            moved[(ny,nx)] = k
        else:
            del shark[k]
            
    for i,j in smell_q:
        if smell_q[(i,j)] > 1:
            q[(i,j)] = smell_q[(i,j)] - 1
        else:
            visited[i][j] = 0

    for i,j in moved:
        visited[i][j] = moved[(i,j)]
        q[(i,j)] = K
    return q
        

n,m,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
direction = [0] + list(map(int,input().split()))
shark_move= {}
for i in range(1,m+1):
    shark= {}
    for j in range(1,5):
        shark[j] = list(map(int,input().split()))
    shark_move[i] = shark
my = {1:-1,2:1,3:0,4:0}
mx = {1:0,2:0,3:-1,4:1}

visited = [[0] * n for _ in range(n)]
shark = {}
smell_q = {}

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            shark[matrix[i][j]] = (i,j,direction[matrix[i][j]])
            visited[i][j] = matrix[i][j]
            smell_q[(i,j)]=K

possible = False
for c in range(1001):
    if len(shark) == 1:
        possible = True
        print(c)
        break
    smell_q = bfs(smell_q)
# 1001초에서는 무조건 -1인데 1001초일 때 len(shark) == 1 이 되는 것을 거르지 못했다
if not possible:
    print(-1)
    
###################### 첫 통과 코드 ######################
def bfs(smell):
    moved = {}
    q = {}
    for s in range(1,m+1):
        if s not in shark: continue
        y,x,d = shark[s]
        ny,nx,nd = -1,-1,-1
        for move_d in shark_move[s][d]:
            dy, dx = y + my[move_d], x + mx[move_d]
            if 0 <= dy < n and 0 <= dx < n:
                if not visited[dy][dx]:
                    ny,nx,nd = dy,dx,move_d
                    break
        if ny == -1:
            for move_d in shark_move[s][d]:
                dy, dx = y + my[move_d], x + mx[move_d]
                if 0 <= dy < n and 0 <= dx < n:
                    if visited[dy][dx] == s:
                        ny,nx,nd = dy,dx,move_d
                        break
        if (ny,nx) not in moved:
            moved[(ny,nx)] = s
            shark[s] = (ny,nx,nd)
        else:
            del shark[s]
    for i,j in smell:
        if smell[(i,j)] > 1:
            q[(i,j)] = smell[(i,j)] - 1
        else:
            visited[i][j] = 0
    for i,j in moved:
        q[(i,j)] = K
        visited[i][j] = moved[(i,j)]
    return q


n,m,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
direction = [0] + list(map(int,input().split()))
shark_move = {i:{ j:list(map(int,input().split())) for j in range(1,5)} for i in range(1,m+1)}
shark = {}
visited = [[0] * n for _ in range(n)]
my = {1:-1,2:1,3:0,4:0}
mx = {1:0,2:0,3:-1,4:1}
smell = {}
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            shark[matrix[i][j]] = (i,j,direction[matrix[i][j]])
            visited[i][j] = matrix[i][j]
            smell[(i,j)] = K
            

possible = False
for c in range(1001):
    if len(shark) == 1:
        possible = True
        print(c)
        break
    smell = bfs(smell)
if not possible:
    print(-1)
