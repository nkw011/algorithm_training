# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-14676
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-14676/

import sys
def input(): return sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
buildings = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

possible = True
for _ in range(k):
    a, b = map(int, input().split())
    if a == 1:
        for prev in graph[b]:
            if not buildings[prev]:
                possible = False
        if possible:
            buildings[b] += 1
    else:
        if not buildings[b]:
            possible = False
        if possible:
            buildings[b] -= 1
if possible:
    print("King-God-Emperor")
else:
    print("Lier!")
