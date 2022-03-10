# i-1, j-1 일 때 IndexError를 피하기 위해 시작 위치 (1,1) => 모든 위치의 인덱스를 1씩 늘림
# 가로가 n 세로가 m => road[m][n]
# 양방향 길이 모두 막혔을 경우를 고려하기 위해 defaultdict(set)을 이용

import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
construction = defaultdict(set)
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a, b, c, d = a+1, b+1, c+1, d+1
    if c-a > 0 or d-b > 0:
        construction[(d, c)].add((b, a))
    elif a-c > 0 or b-d > 0:
        construction[(b, a)].add((d, c))

road = [[0] * (n+2) for _ in range(m+2)]
road[1][1] = 1
for i in range(1, m+2):
    for j in range(1, n+2):
        if road[i][j] != 0:
            continue
        if (i-1, j) not in construction[(i, j)]:
            road[i][j] += road[i-1][j]
        if (i, j-1) not in construction[(i, j)]:
            road[i][j] += road[i][j-1]

print(road[m+1][n+1])
