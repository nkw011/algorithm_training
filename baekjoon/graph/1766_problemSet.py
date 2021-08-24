# 전형적인 위상정렬 문제
# 문제 난이도가 낮은 순서부터라고 해서 dfs를 이용해 뒤에서 부터 푸는 방식으로 했지만 틀렸습니다가 나옴
# q를 활용한 방식으로 변경해서 문제 난이도가 낮은 순서부터 해야하기 때문에 heapq를 이용해 구현하였다.


import sys
import heapq
def input(): return sys.stdin.readline().rstrip()


def topology():
    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    while q:
        w = heapq.heappop(q)
        for nxt in graph[w]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(q, nxt)
        print(w, end=' ')
    print()


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology()
