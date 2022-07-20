# 풀이 및 해설 1: https://velog.io/@nkw011/baekjoon-2234
# 풀이 및 해설 2: https://nkw011.github.io/baekjoon/baekjoon-2234/

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def bfs(i, j, number):
    q = deque([(i,j,1)])
    splitted[i][j] = number
    result = [(i, j)]
    while q:
        y, x, area = q.popleft()
        for idx in range(4):
            if matrix[y][x] & (1 << idx): continue
            dy, dx = y + my[idx], x + mx[idx]
            if 0 <= dy < m and 0 <= dx < n and not splitted[dy][dx]:
                splitted[dy][dx] = number
                result.append((dy, dx))
                q.append((dy,dx,area+1))
    return len(result)

def find_connected_area():
    visited = [[0] * n for _ in range(m)]
    q = deque([(0,0, splitted[0][0])])
    max_area = 0
    while q:
        y, x, number1 = q.popleft()
        for idx in range(4):
            dy, dx = y + my[idx], x + mx[idx]
            if 0 <= dy < m and 0 <= dx < n and not visited[dy][dx]:
                number2 = splitted[dy][dx]
                visited[dy][dx] = 1
                q.append((dy,dx,number2))
                if number1 != number2 and max_area < (areas[number1] + areas[number2]):
                    max_area = areas[number1] + areas[number2]
    return max_area

n, m = map(int,input().split()) # 너비, 높이
matrix = [ list(map(int,input().split())) for _ in range(m)]
my = [0,-1,0,1]
mx = [-1,0,1,0]

splitted = [[0] * n for _ in range(m)]
cnt = 0
areas = [0]
for i in range(m):
    for j in range(n):
        if not splitted[i][j]:
            cnt += 1
            areas.append(bfs(i,j,cnt))

print(cnt)
print(max(areas))
print(find_connected_area())
