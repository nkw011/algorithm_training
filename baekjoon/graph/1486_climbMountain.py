# 처음 dp를 사용했을 때 왜 되지 않았냐면 방향을 정해놓고 reverse 하는 방식을 적용해서 구현을 하였는데
# 모든 방향에서 적용이 가능하므로 dp가 사용이 불가능하다는 것을 알게되었다.

# 따라서, dijkstra를 이용해서 구현하는 방식으로 바꿨고
# 1 -> (i,j)로 (i,j) - >1 로 가는 최단 시간을 위해서 합한 시간이 d 인것중 제일 높은 높이를 출력하였다.

# 비교값을 설정해서 값을 갱신할 때 비교값의 초기값을 잘 설정해야한다는 것을 알게되었다.
# 또한 > 와 - 를 계속해서 오타를 내고 있는데
# 이 점 주의해서 구현을 해야겠다.

import sys
import heapq
INF = int(1e12)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(i, j, dist):
    dist[i][j] = 0
    q = []
    heapq.heappush(q, (dist[i][j], i, j))
    while q:
        dt, y, x = heapq.heappop(q)
        if dist[y][x] < dt:
            continue
        for idx in range(4):
            dy = y + my[idx]
            dx = x + mx[idx]
            if 0 <= dy < n and 0 <= dx < m:
                if abs(mountain[dy][dx] - mountain[y][x]) <= t:
                    if mountain[dy][dx] > mountain[y][x] and dist[dy][dx] > dt + (mountain[dy][dx] - mountain[y][x])**2:
                        # 도대체 \ 이게 왜 goorm에서는 오류라고 뜨는 지 잘모르겠다.
                        dist[dy][dx] = dt + \
                            (mountain[dy][dx] - mountain[y][x])**2
                        if dist[dy][dx] > d:
                            continue
                        heapq.heappush(q, (dist[dy][dx], dy, dx))
                    elif mountain[dy][dx] <= mountain[y][x] and dist[dy][dx] > dt + 1:
                        dist[dy][dx] = dt + 1
                        if dist[dy][dx] > d:
                            continue
                        heapq.heappush(q, (dist[dy][dx], dy, dx))


n, m, t, d = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
mountain = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if ord('a') <= ord(matrix[i][j]) <= ord('z'):
            mountain[i][j] = ord(matrix[i][j]) - ord('a') + 26
        else:
            mountain[i][j] = ord(matrix[i][j]) - ord('A')

my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]

dp1 = [[INF] * m for _ in range(n)]
dp2 = [[INF] * m for _ in range(n)]
dijkstra(0, 0, dp1)
r = mountain[0][0]
for i in range(n):
    for j in range(m):
        if dp1[i][j] != INF and dp1[i][j] < d:
            dp2 = [[INF] * m for _ in range(n)]
            dijkstra(i, j, dp2)
            if dp1[i][j] + dp2[0][0] > d:
                continue
            r = max(mountain[i][j], r)

print(r)
