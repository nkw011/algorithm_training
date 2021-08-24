# 예상되는 답을 찾기에는 너무 오래걸릴때
# 이분탐색을 생각해보자..
# 생각보다 탐색에 이분탐색을 응용하는 것이 많다.


from collections import deque
import sys
INF = int(1e4)
def input(): return sys.stdin.readline().rstrip()


def path(start, end, interval):
    for s in range(start, end+1):
        if bfs(s, s+interval):
            return True
    return False


def bfs(s, e):
    q = deque()
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    if s <= matrix[0][0] <= e:
        q.append((0, 0))
    while q:
        r, c = q.popleft()
        if r == n-1 and c == n-1:
            return True
        for idx in range(4):
            dy = r + my[idx]
            dx = c + mx[idx]
            if 0 <= dy < n and 0 <= dx < n:
                if s <= matrix[dy][dx] <= e and not visited[dy][dx]:
                    visited[dy][dx] = 1
                    q.append((dy, dx))
    return False


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]

left = 0
minValue = 201
right = -201
for i in range(n):
    for j in range(n):
        if matrix[i][j] > right:
            right = matrix[i][j]
        if matrix[i][j] < minValue:
            minValue = matrix[i][j]
maxValue = right

result = 0
while left <= right:
    mid = (left+right) // 2
    if path(minValue, maxValue, mid):
        right = mid-1
        result = mid
    else:
        left = mid+1
print(result)
