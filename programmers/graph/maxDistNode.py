# https://programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque


def solution(n, edges):
    g = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    q = deque([1])
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    visited[1] = 1
    maxValue = 1
    while q:
        w = q.popleft()
        for nxt in g[w]:
            if not visited[nxt]:
                visited[nxt] = visited[w] + 1
                maxValue = max(visited[nxt], maxValue)
                q.append(nxt)

    return visited.count(maxValue)
