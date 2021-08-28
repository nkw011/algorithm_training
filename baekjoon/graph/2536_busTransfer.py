# 안 만나는 경우를 체크하는 것이 훨씬 구현도 간단하고 코드 길이도 준다.
# 거의 3주만에 하는 것이라 많이 부족하다...

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def bfs():
    q = deque(start)
    while q:
        line, cnt = q.popleft()
        if buscircuit[line][0] <= tx <= buscircuit[line][2] and buscircuit[line][1] <= ty <= buscircuit[line][3]:
            return cnt
        for nxt in graph[line]:
            if not visited[nxt]:
                # 방문 체크후 방문 처리를 해주지 않았다... 그래서 계속 메모리초과 발생
                visited[nxt] = 1
                q.append((nxt, cnt+1))
    return -1


def intersection(t1, t2):
    if t1[4] == 0:
        return (t1[0], t2[1])
    else:
        return (t2[0], t1[1])


def include(x, y, line):
    if line[0] <= x <= line[2] and line[1] <= y <= line[3]:
        return True
    return False


def parallelInclude(line1, line2):
    if line1[4] == 0 and line1[0] == line2[0]:
        if line1[1] <= line2[1] <= line1[3] or line1[1] <= line2[3] <= line1[3]:
            return True
        if line2[1] <= line1[1] <= line2[3] or line2[1] <= line1[3] <= line2[3]:
            return True
    if line1[4] == 1 and line1[1] == line2[1]:
        if line1[0] <= line2[0] <= line1[2] or line1[0] <= line2[2] <= line1[2]:
            return True
        if line2[0] <= line1[0] <= line2[2] or line2[0] <= line1[2] <= line2[2]:
            return True
    return False


n, m = map(int, input().split())
k = int(input())

buscircuit = [0] * (k+1)
graph = [[] for _ in range(k+1)]
visited = [0] * (k+1)
start = []

for _ in range(k):
    idx, x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        mx = max(y1, y2)
        mn = min(y1, y2)
        buscircuit[idx] = (x1, mn, x2, mx, 0)
    elif y1 == y2:
        mx = max(x1, x2)
        mn = min(x1, x2)
        buscircuit[idx] = (mn, y1, mx, y2, 1)

sx, sy, tx, ty = map(int, input().split())

# check if each line is parallel
for i in range(1, k+1):
    if buscircuit[i][0] <= sx <= buscircuit[i][2] and buscircuit[i][1] <= sy <= buscircuit[i][3]:
        start.append((i, 1))
        visited[i] = 1
    for j in range(1, k+1):
        if i == j:
            continue
        # 라인이 평행한경우: 포함하는 지 확인
        if buscircuit[i][4] == buscircuit[j][4]:
            if parallelInclude(buscircuit[i], buscircuit[j]):
                graph[i].append(j)
        else:
            # 라인이 평행하지 않은 경우 : 교차점이 발생하는 지 확인
            x, y = intersection(buscircuit[i], buscircuit[j])
            if include(x, y, buscircuit[i]) and include(x, y, buscircuit[j]):
                graph[i].append(j)

print(bfs())
