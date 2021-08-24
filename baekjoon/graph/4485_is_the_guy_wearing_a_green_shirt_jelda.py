# 완전 탐색 상에서 한 정점에서 다른 정점까지의 최단거리를 구하는 것이다.
# 일반적인 bfs로 풀 수 없었던 이융는 가중치가 있었기 때문이다.
# 가중치가 있는 곳에서의 최단거리는 역시 heapq를 이용한 다익스트라가 맞다.
# 다익스트라를 이용하면 풀 수가 있었다... (다익스트라의 신기한 응용인것같다.)

# 다익스트라는 신기하게도 q에서 pop 되는 것이 가장 거리가 짧은 그 다음 노드기 때문에
# pop되고 나서 나오는 원소에 대해 방문체크를 해주어야한다. 
# 미리 방문체크를 하는 일반 bfs랑은 많이 다른 것 같다.

# 거리로 방문체크를 하는 경우는 최단 거리가 새로 갱신이 되었을 경우에 heapq에 넣는 것이다.

import sys
input = lambda : sys.stdin.readline()
INF = 9 * 125**3
import heapq

def dijkstra():
    q = [(matrix[0][0],0,0)]
    distances[0][0] = matrix[0][0]
    while q:
        dist,i,j = heapq.heappop(q)
        if i == n-1 and j == n-1:
            return dist
        if not visited[i][j]:
            visited[i][j] = 1
            for index in range(4):
                dx = j + mx[index]
                dy = i + my[index]
                if 0 <= dy < n and 0 <= dx < n:
                    distances[dy][dx] = min(distances[dy][dx],matrix[dy][dx] + dist)
                    heapq.heappush(q,(distances[dy][dx],dy,dx))
    return -1
loop = 0
mx = [1,-1,0,0]
my = [0,0,1,-1]

while True:
    loop += 1
    n = int(input())
    if n == 0:
        break
    matrix = [list(map(int,input().split())) for _ in range(n)]
    distances = [[INF] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    print("Problem {0}: {1}".format(loop,dijkstra()))