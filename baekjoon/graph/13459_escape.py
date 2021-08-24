import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

# 예를 들어 어떤 걸 움직일 때...
# 뭐가 왼쪽으로 기울일 때는 뭐가 더 왼쪽에 있는 지 생각해서 그거 먼저 굴려야한다.
# 따라서 기능별 움직이는 함수는 따로 만들면 될 것 같다.


def moveLeft(ry,rx,by,bx):
    nry,nrx,nby,nbx = ry,rx,by,bx
    for j in range(bx-1,-1,-1):
        if matrix[by][j] == '.':
            nby,nbx = by,j
        elif matrix[by][j] == 'O':
            nby,nbx = by,j
            break
        else :
            break
    for j in range(rx-1,-1,-1):
        if matrix[ry][j] == '.':
            nry,nrx = ry,j
        elif matrix[ry][j] == 'O':
            nry,nrx = ry,j
            break
        else :
            break
    return (nry,nrx,nby,nbx)

def moveRight(ry,rx,by,bx):
    nry,nrx,nby,nbx = ry,rx,by,bx
    for j in range(bx+1,m):
        if matrix[by][j] == '.':
            nby,nbx = by,j
        elif matrix[by][j] == 'O':
            nby,nbx = by,j
            break
        else :
            break
    for j in range(rx+1,m):
        if matrix[ry][j] == '.':
            nry,nrx = ry,j
        elif matrix[ry][j] == 'O':
            nry,nrx = ry,j
            break
        else :
            break
    return (nry,nrx,nby,nbx)

def moveUp(ry,rx,by,bx):
    nry,nrx,nby,nbx = ry,rx,by,bx
    for i in range(by-1,-1,-1):
        if matrix[i][bx] == '.':
            nby,nbx = i,bx
        elif matrix[i][bx] == 'O':
            nby,nbx = i,bx
            break
        else :
            break
    for i in range(ry-1,-1,-1):
        if matrix[i][rx] == '.':
            nry,nrx = i,rx
        elif matrix[i][rx] == 'O':
            nry,nrx = i,rx
            break
        else :
            break
    return (nry,nrx,nby,nbx)

def moveDown(ry,rx,by,bx):
    nry,nrx,nby,nbx = ry,rx,by,bx
    for i in range(by+1,n):
        if matrix[i][bx] == '.':
            nby,nbx = i,bx
        elif matrix[i][bx] == 'O':
            nby,nbx = i,bx
            break
        else :
            break
    for i in range(ry+1,n):
        if matrix[i][rx] == '.':
            nry,nrx = i,rx
        elif matrix[i][rx] == 'O':
            nry,nrx = i,rx
            break
        else :
            break
    return (nry,nrx,nby,nbx)
def bfs():
    q = deque()
    q.append((ry,rx,by,bx,0))
    while q:
        qry,qrx,qby,qbx,count = q.popleft()
        if count > 10 : continue
        if matrix[qby][qbx] == 'O' : return 0
        if matrix[qry][qrx] == 'O': return 1
        
        nry,nrx,nby,nbx = moveLeft(qry,qrx,qby,qbx)
        if nry != nby and nrx != nbx :
            q.append((nry,nrx,nby,nbx,count+1))
            
        nry,nrx,nby,nbx = moveRight(qry,qrx,qby,qbx)
        if nry != nby and nrx != nbx :
            q.append((nry,nrx,nby,nbx,count+1))
            
        nry,nrx,nby,nbx = moveUp(qry,qrx,qby,qbx)
        if nry != nby and nrx != nbx :
            q.append((nry,nrx,nby,nbx,count+1))
            
        nry,nrx,nby,nbx = moveDown(qry,qrx,qby,qbx)
        if nry != nby and nrx != nbx :
            q.append((nry,nrx,nby,nbx,count+1))
    return 0

n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
ry,rx,by,bx = -1,-1,-1,-1

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            ry,rx = i,j
        elif matrix[i][j] == 'B':
            by,bx = i,j
            
print(bfs())