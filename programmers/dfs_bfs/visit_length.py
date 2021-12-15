# https://programmers.co.kr/learn/courses/30/lessons/49994
# 간단한 BFS문제이다...
# 조건을 잘 파악해서 구현하자

def solution(dirs):
    visited = set()
    move = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    n,m,x,y = -5,5,0,0
    for d in dirs:
        dx,dy = move[d][0] + x, move[d][1] + y
        if n <= dy <=m and n <= dx <= m:
            if (x,y,dx,dy) not in visited and (dx,dy,x,y) not in visited:
                visited.add((x,y,dx,dy))
            y,x = dy,dx
    return len(visited)
