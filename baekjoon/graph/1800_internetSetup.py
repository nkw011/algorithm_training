# 교훈 : 전체 탐색시 이분탐색(결정문제)을 한 번 고려해보자!!!
# 분류에 대한 힌트가 없었다면 절대 풀지 못했을 문제이다.
# 분류: 이분 탐색, 다익스트라
# 앞으로 최단거리인데 전체를 탐색해야할 것 같으면 이분 탐색을 써보는 것도 나쁘진 않을 듯

import sys
import heapq
INF = int(1e11)
def input(): return sys.stdin.readline().rstrip()


def dijkstra(limit):
    dist[1][0] = 0
    q = []
    heapq.heappush(q, (0, 1, 0))
    while q:
        d, w, cnt = heapq.heappop(q)
        if dist[w][cnt] < d:
            continue
        if w == n:
            return True
        for nxt, cost in graph[w]:
            if cost > limit:
                if cnt + 1 <= k and dist[nxt][cnt+1] > d+cost:
                    dist[nxt][cnt+1] = d + cost
                    heapq.heappush(q, (d+cost, nxt, cnt+1))
            else:
                if dist[nxt][cnt] > d+cost:
                    dist[nxt][cnt] = d+cost
                    heapq.heappush(q, (d+cost, nxt, cnt))
    return False


n, p, k = map(int, input().split())
maxDist = 0
graph = [[] for _ in range(n+1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    maxDist = max(maxDist, c)
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [[INF] * (k+1) for _ in range(n+1)]
left = 0
right = maxDist+1

result = INF
while left <= right:
    mid = (left+right) // 2
    dist = [[INF] * (k+1) for _ in range(n+1)]
    if dijkstra(mid):
        right = mid - 1
        result = mid
    else:
        left = mid + 1

if result == INF:
    print(-1)
else:
    print(result)
