# 분명 생각한 아이디어인데
# 왜 주저하게 되는 걸까?

import sys
INF = int(1e10)
def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
dist = [[INF] * (n+1) for _ in range(n+1)]
edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    dist[b][a] = min(dist[b][a], c)
    edge.append((a, b, c))

for i in range(1, n+1):
    dist[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

best = INF
for w in range(1, n+1):
    result = 0
    for a, b, c in edge:
        minTime = min(dist[w][a], dist[w][b])
        maxTime = max(dist[w][a], dist[w][b])
        if minTime + c <= maxTime:
            result = max(minTime+c, result)
        else:
            result = max((minTime+c - maxTime) / 2 + maxTime, result)
    best = min(best, result)
# 정수일경우 소수로 출력을 하지 못해서 발생하는 일이었다.
print(float(best))
