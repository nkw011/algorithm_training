# 그래프의 노드는 아무거나 될 수 있다는 것을 깨닫자!!
# 왜 이 쉬운 사실을 난 알지 못하는 것인가...

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def bfs(s):
    visited[s] = 1
    q = deque()
    q.append(s)
    while q:
        w = q.popleft()
        if w == n:
            return visited[n]
        for nxt in graph[w]:
            if not visited[nxt]:
                q.append(nxt)
                if nxt > n:
                    visited[nxt] = visited[w]
                else:
                    visited[nxt] = visited[w] + 1
    return -1


n, k, m = map(int, input().split())
graph = [[] for _ in range(n+m+1)]
visited = [0] * (n+m+1)
for i in range(1, m+1):
    nums = list(map(int, input().split()))
    for num in nums:
        graph[n+i].append(num)
        graph[num].append(n+i)

print(bfs(1))
