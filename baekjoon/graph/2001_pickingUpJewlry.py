import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def bfs():
    visited[1][0] = 1
    result = 0
    q = deque()
    q.append((1, 0, 0))
    while q:
        w, get, count = q.popleft()
        if w == 1:
            result = max(result, count)
        for nxt, c in graph[w]:
            if count <= c and not visited[nxt][get]:
                visited[nxt][get] = 1
                q.append((nxt, get, count))
            if gem[nxt]:
                # 보석을 얻는 것은 가서 얻는 것이니까
                # 건널 때 count +1 을 할 필요가 없다...
                # 이걸로 3시간 날렸다... 역시 대충 짜는게 아니라 의식적으로 짤 필요가 있다.
                if count > c:
                    continue
                if not visited[nxt][get | (1 << gem[nxt])]:
                    visited[nxt][get | (1 << gem[nxt])] = 1
                    if get & (1 << gem[nxt]):
                        continue
                    q.append((nxt, get | (1 << gem[nxt]), count+1))

    return result


n, m, k = map(int, input().split())
gem = [0] * (n+1)
graph = [[] for _ in range(n+1)]
count = 1
visited = [[0] * ((1 << (k+1))) for _ in range(n+1)]

for _ in range(k):
    gem[int(input())] = count
    count += 1

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(bfs())
