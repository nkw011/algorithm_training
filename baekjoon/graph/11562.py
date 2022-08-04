# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-11562
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-11562/

import sys
INF = int(1e14)
def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c:
        graph[a][b] = 0
        graph[b][a] = 0
    else:
        graph[a][b] = 0
        graph[b][a] = 1

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(graph[s][e])ㅍ
