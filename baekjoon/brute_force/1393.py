# 풀이 및 해설: https://nkw011.github.io/baekjoon/baekjoon-1254/

import sys
def input(): return sys.stdin.readline().rstrip()

def func(x):
    grad = dy / dx
    return  grad * x - grad * x_e + y_e
def distance(x1,y1,x2,y2):
    return ((x1-x2) ** 2 + (y1-y2)**2)**(1/2)

x_s, y_s = map(int,input().split())
x_e, y_e, dx, dy = map(int,input().split())

min_d,x,y = distance(x_e,y_e,x_s,y_s),x_e,y_e
if dx > 0:
    for i in range(x_e,1001):
        if distance(i,func(i),x_s,y_s) < min_d:
            min_d = distance(i, int(func(i)),x_s,y_s)
            x,y = i, int(func(i))
elif dx < 0:
    for i in range(x_e,-1001,-1):
        if distance(i,func(i),x_s,y_s) < min_d:
            min_d = distance(i, int(func(i)),x_s,y_s)
            x,y = i, int(func(i))
elif dy > 0:
    for i in range(y_e,1001):
        if distance(x_e,i,x_s,y_s) < min_d:
            min_d = distance(x_e,i,x_s,y_s)
            x,y = x_e, i
else:
    for i in range(y_e,-1001,-1):
        if distance(x_e,i,x_s,y_s) < min_d:
            min_d = distance(x_e,i,x_s,y_s)
            x,y = x_e,i
print(x,y)
