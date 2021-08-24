# 가중치 문제가 아니기 때문에 heapq를 쓸 필요가 없다.
# 이것때문에 계속 시간초과가 나왔네...

import sys
input = sys.stdin.readline
from collections import deque

def D(num):
    return (num * 2) % 10000
def S(num):
    if num == 0:
        return 9999
    return num - 1

def L(num):
    if num < 1000:
        return num * 10
    else:
        d1,d2,d3,d4 = num //1000 , (num//100) % 10, (num //10)% 10, num % 10
        return ((d2 * 10 + d3) * 10 + d4) * 10 + d1

def R(num):
    if num < 10:
        return num * 1000
    else :
        return (num % 10) * 1000 + (num // 10)

def bfs():
    global a,b
    visited = [0] * 10000
    matrix = [0] * 10000
    visited[a] = 1
    matrix[a] =(10000,'')
    q = deque([a])
    while q:
        num = q.popleft()
        if num == b:
            result = []
            while matrix[num][0] != 10000 :
                result.append(matrix[num][1])
                num = matrix[num][0]
            for i in range(len(result)-1,-1,-1):
                print(result[i],end='')
            print()
            return
        num1,num2,num3,num4 = D(num),S(num),L(num),R(num)
        if not visited[num1]:
            visited[num1] = 1
            q.append(num1)
            matrix[num1] = (num,'D')
        if not visited[num2]:
            visited[num2] = 1
            q.append(num2)
            matrix[num2] = (num,'S')
        if not visited[num3]:
            visited[num3] = 1
            q.append(num3)
            matrix[num3] = (num,'L')
        if not visited[num4]:
            visited[num4] = 1
            q.append(num4)
            matrix[num4] = (num,'R')
    return
    
T = int(input().rstrip())
for _ in range(T):
    a,b = map(int,input().split())
    bfs()