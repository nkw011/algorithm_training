# 2610_prepareMeeting.py

# 결국 의사전달 시간이라는 것은 각 대표로 부터 떨어진 거리를 의미하므로
# 최단거리 구하기 알고리즘을 응용하여 풀 수 있을 것 같다.

# 그래프를 보고 어떤 걸 해야하는 지 잘 파악하도록 하자!!

import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e8)

def dfs(i):
    visited[i] = count
    for nxt in graph[i]:
        if not visited[nxt]:
            dfs(nxt)
    component[count].append(i)

def findMax(i,array):
    ret = -1
    for j in range(1,n+1):
        if j == i:
            continue
        if array[j] != INF and array[j] > ret:
            ret = array[j]
    return ret

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dist = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    dist[a][b] = 1
    dist[b][a] = 1

visited = [0] * (n + 1)
component = [[] for _ in range(n+1)]
count = 0

# 같은 컴포넌트 찾기
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])

print(count)
repr = []
for comp in component:
    now = -1
    cnt = INF
    for candi in comp:
        ret = findMax(candi,dist[candi])
        if cnt > ret:
            cnt = ret
            now = candi
    if now != -1:
        repr.append(now)
repr.sort()
for t in repr:
    print(t)
