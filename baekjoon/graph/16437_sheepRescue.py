# 마지막 시도 : 메모리초과 개선
# pypy3는 메모리를 너무 많이 잡아먹기 때문에 혹시 다른 원인을 못찾겠는데 메모리 초과가 일어난다면 python3로 바꾸어서 하면
# 좋을 것 같다.


import sys
input = __import__('sys').stdin.readline
sys.setrecursionlimit(200000)

def dfs(here):
    if sheep[here] > 0:
        dp[here] = sheep[here]
    else:
        dp[here] = (-1) * wolf[here]
    for nxt in graph[here]:
        if dp[nxt] != -1 and dp[nxt] > 0:
            dp[here] += dp[nxt]
        elif dp[nxt] == -1 and dfs(nxt) > 0:
            dp[here] += dp[nxt]
    return dp[here]


n = int(input())
sheep = [0] * (n+1)
wolf = [0] * (n+1)
graph = [[] for _ in range(n+1)]
dp = [-1] * (n+1)
visited = [0] * (n+1)

for i in range(2, n+1):
    temp = input().split()
    graph[int(temp[2])].append(i)
    if temp[0] == 'S':
        sheep[i] = int(temp[1])
    else:
        wolf[i] = int(temp[1])

print(dfs(1))







#  첫 시도 시간초과 이유 : dijkstra(s)는 O(VlogV)인데 양에서 도착지까지 가는 최단 경로를 각각 탐색했으므로
#  V * O(VlogV)는 1초를 넘어서게된다.

# 두 번째 시도 : 따라서 dijkstra를 그대로 적용하되 시작지 -> 양이 있는 곳으로의 최단경로로 생각해보았다.
# 늑대가 평생 1마리만 먹는다고 한다. 따라서 다른 방식으로 아이디어를 구현할 필요가 있다.

import heapq
import sys
def input(): return sys.stdin.readline().rstrip()

# 원래 dfs 사용시 방문체크를 해주어야하지만 어차피 dp로 풀기 때문에 다른 방문체크는 하지 않는 걸로..
# 파이썬 사용시 메모리 초과가 나지 않도록 해주어야하는데... 너무 힘들다..


def dfs(here):
    if sheep[here] > 0:
        dp[here] = sheep[here]
    else:
        dp[here] = (-1) * wolf[here]
    for nxt in graph[here]:
        if dp[nxt] != -1 and dp[nxt] > 0:
            dp[here] += dp[nxt]
        elif dp[nxt] == -1 and dfs(nxt) > 0:
            dp[here] += dp[nxt]
    return dp[here]


n = int(input())
sheep = [0] * (n+1)
wolf = [0] * (n+1)
graph = [[] for _ in range(n+1)]
dp = [-1] * (n+1)

for i in range(2, n+1):
    temp = input().split()
    graph[int(temp[2])].append(i)
    if temp[0] == 'S':
        sheep[i] = int(temp[1])
    else:
        wolf[i] = int(temp[1])

print(dfs(1))


############################ 첫번째 및 두번째 시도 #################################
# INF = int(1e10)
# def input(): return sys.stdin.readline().rstrip()


# def dijkstra(s):
#     dist[s] = 0
#     q = []
#     heapq.heappush(q, (dist[s], s))
#     while q:
#         d, w = heapq.heappop(q)
#         if d > dist[w]:
#             continue
#         for nxt, cost in graph[w]:
#             if dist[nxt] > d + cost:
#                 dist[nxt] = d + cost
#                 heapq.heappush(q, (dist[nxt], nxt))
#     return INF


# n = int(input())
# graph = [[] for _ in range(n+1)]
# sheep = [0] * (n+1)
# dist = [INF] * (n+1)

# for i in range(2, n+1):
#     temp = input().split()
#     cost, nxt = int(temp[1]), int(temp[2])
#     if temp[0] == 'S':
#         sheep[i] = cost
#         graph[nxt].append((i, 0))
#     else:
#         graph[nxt].append((i, cost))

# dijkstra(1)
# result = 0
# for i in range(2, n+1):
#     if sheep[i] > 0 and sheep[i] > dist[i]:
#         result += (sheep[i] - dist[i])
# print(result)
