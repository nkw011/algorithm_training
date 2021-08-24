import sys
def input(): return sys.stdin.readline().rstrip()


# 메모리초과는 python3를 이용하여 해결하였다.
# n이 최대 1000000이기 때문에 limit을 1000000으로 설정하였다.
sys.setrecursionlimit(1000000)

EARLY = 0
NOTEARLY = 1


def dfs(i):
    global result
    cnt = [0, 0]
    visited[i] = 1
    for nxt in graph[i]:
        if not visited[nxt]:
            cnt[dfs(nxt)] += 1
    # 사실 파악해보면 별거 아닌 관계였다.
    # 상대방 중 early가 아닌 사람이 1명이라도 있으면 내가 early여야하고
    # 없으면 early여도 되고 아니여도 된다.
    if cnt[NOTEARLY] > 0:
        status[i] = EARLY
        result += 1
    elif cnt[EARLY] > 0:
        status[i] = NOTEARLY
    return status[i]


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
status = [-1] * (n+1)
visited = [0] * (n+1)

result = 0
for p in range(1, n+1):
    if not visited[p]:
        dfs(p)

result = 0
for i in range(1, n+1):
    if status[i] == EARLY:
        result += 1
print(result)
