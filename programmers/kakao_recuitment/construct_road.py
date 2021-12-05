# https://programmers.co.kr/learn/courses/30/lessons/67259

# 해결방안 
# 1. weight가 있는 graph에서 최단 경로를 찾는 것이므로 dijkstra를 활용하여 거리를 구한다.
# 2. 방향표시 0,1 : 1 -> 상 하, 0 -> 좌 우
# 3. Node : i,j, cost로 나타낸다.
# 4. 상 하에서 들어왔을 때의 비용과 좌 우에서 들어왔을 때의 비용 중 작은 값을 출력한다.

import heapq

my = [1,-1,0,0]
mx = [0,0,1,-1]

def solution(board):
    INF,n = 1e10, len(board)
    cost,q = [[[INF] * 2 for _ in range(n)] for _ in range(n)], []
    heapq.heappush(q,(0,0,0,-1))
    while q:
        y,x,c,d = heapq.heappop(q)
        if cost[y][x][d] < c:
            continue
        for i in range(4):
            dy = y + my[i]
            dx = x + mx[i]
            if 0 <= dy < n and 0 <= dx < n and not board[dy][dx]:
                if d == -1:
                    cost[dy][dx][abs(my[i])] = 100
                    heapq.heappush(q,(dy,dx,100,abs(my[i])))
                else:
                    temp = c+ 100 if d == abs(my[i]) else c + 100 + 500
                    if cost[dy][dx][abs(my[i])] > temp:
                        cost[dy][dx][abs(my[i])] = temp
                        heapq.heappush(q,(dy,dx,temp,abs(my[i])))
    return min(cost[n-1][n-1])
