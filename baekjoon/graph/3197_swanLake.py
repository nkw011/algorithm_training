# 그래프 정점 내 최단거리가 아닌 매트릭스 형태 최단거리는
# heapq를 사용하면 오히려 heappush할 때마다 일어나는 정렬로 인해
# 시간이 더 걸릴 수 있다.

import sys
import heapq
from collections import deque
INF = 1500 * 1500
def input(): return sys.stdin.readline().rstrip()

# 일단 heapq에서 시간초과가 나온다는 것을 알았다.(이걸로 시간초과라는 걸 5번 시간초과나서(약 3시간) 알게되었다.)
# 매번 비슷한 값을 계속 집어넣는데는 heapq가 비효율적이라는 것을 알게되었다.
def melting():
    ret = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            # 백조가 있는 곳도 물이기 때문에 백조 근방의 빙하들은 녹아서 없어진다.
            # 오늘도 많이 배웠습니다.
            if matrix[i][j] == '.' or matrix[i][j] == 'L':
                visited[i][j] = 0
                q.append((0,i,j))
    while q:
        day,r,c = q.popleft()
        if ret < day:
            ret = day
        for idx in range(4):
            dy = r + my[idx]
            dx = c + mx[idx]
            if 0 <= dy < n and 0 <=dx < m:
                if matrix[dy][dx] == 'X':
                    if visited[dy][dx] == -1:
                        visited[dy][dx] = day +1
                        q.append((day+1,dy,dx))
    return ret

# 이렇게 하려면 일반 q로 돌려야한다.                        
# 이분탐색으로 찾는 방법이 있다고 한다.
def move(sy,sx, limit):
    discovered = [[0] * m for _ in range(n)]
    q = deque()
    discovered[sy][sx] = 1
    q.append((sy,sx))
    while q:
        r,c = q.popleft()
        for idx in range(4):
            dy = r + my[idx]
            dx = c + mx[idx]
            if 0 <= dy < n and 0 <= dx < m:
                if not discovered[dy][dx]:
                    discovered[dy][dx] = 1
                    if matrix[dy][dx] == 'L':
                        return True
                    if visited[dy][dx] <= limit:
                        q.append((dy,dx))
    return False


n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
my = [1,-1,0,0]
mx = [0,0,1,-1]

sy,sx = -1,-1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'L':
            sy,sx = i,j
            break
    if sy != -1:
        break

left = 0
right = melting()
result = 0

# 전체를 돌면서 갱신하기에는 값이 너무 크므로
# 이분 탐색을 하면서 시간을 줄인다. (그렇네... 이분 탐색으로 줄였어야했네)
while left <= right:
    mid = (left + right) // 2
    if move(sy,sx,mid):
        result = mid
        right = mid -1
    else:
        left = mid + 1
        
print(result)