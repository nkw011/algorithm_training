# 요구사항을 충싫히 분석을 해야한다는 것을 알려준 문제이다.
# 처음 방식대로 단순히 분석해서 제출했다가는 바로 '틀렸습니다'가 나올 뻔 했다.
# 이 문제를 통해 많이 알게되었다.


import sys
import heapq
INF = int(1e15)
def input(): return sys.stdin.readline().rstrip()


def dijkstra():
    q = []
    t[1] = 0
    heapq.heappush(q, (t[1], 1))
    while q:
        d, w = heapq.heappop(q)
        if t[w] < d:
            continue
        for nxt in range(1, n+1):
            if not dist[w][nxt]:
                continue
            if not congest[w][nxt]:
                if t[nxt] > t[w] + dist[w][nxt]:
                    t[nxt] = t[w] + dist[w][nxt]
                    heapq.heappush(q, (t[nxt], nxt))
                continue
            if t[w] < s:
                if t[w] + dist[w][nxt] < s:
                    if t[nxt] > t[w] + dist[w][nxt]:
                        t[nxt] = t[w] + dist[w][nxt]
                        heapq.heappush(q, (t[nxt], nxt))
                elif s + 2*(dist[w][nxt] - (s-t[w])) <= e:
                    if t[nxt] > s + 2*(dist[w][nxt] - (s-t[w])):
                        t[nxt] = s + 2*(dist[w][nxt] - (s-t[w]))
                        heapq.heappush(q, (t[nxt], nxt))
                else:
                    if t[nxt] > e + dist[w][nxt] - (e-s)/2 - (s-t[w]):
                        t[nxt] = e + dist[w][nxt] - (e-s)/2 - (s-t[w])
                        heapq.heappush(q, (t[nxt], nxt))
            elif s <= t[w] < e:
                if t[w] + 2 * dist[w][nxt] <= e:
                    if t[nxt] > t[w] + 2 * dist[w][nxt]:
                        t[nxt] = t[w] + 2 * dist[w][nxt]
                        heapq.heappush(q, (t[nxt], nxt))
                else:
                    if t[nxt] > e + dist[w][nxt] - (e-t[w])/2:
                        t[nxt] = e + dist[w][nxt] - (e-t[w]) / 2
                        heapq.heappush(q, (t[nxt], nxt))
            else:
                if t[nxt] > t[w] + dist[w][nxt]:
                    t[nxt] = t[w] + dist[w][nxt]
                    heapq.heappush(q, (t[nxt], nxt))


n, m, s, e = map(int, input().split())
dist = [[0] * (n+1) for _ in range(n+1)]
congest = [[0] * (n+1) for _ in range(n+1)]
t = [INF] * (n+1)

for _ in range(m):
    a, b, l, t1, t2 = map(int, input().split())
    dist[a][b] = l
    dist[b][a] = l
    if t1:
        congest[a][b] = 1
    if t2:
        congest[b][a] = 1

dijkstra()

r = max(t[1:])
if int(r) == r:
    print(int(r))
else:
    print(r)
