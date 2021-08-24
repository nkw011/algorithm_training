# 위상정렬에 대해 다시 배우는 것 같다.
# 위상정렬의 조건은 DAG여야한다는 것(즉, 사이클이 발생하면 안된다.)
# dfs를 활용한 위상정렬 구현시 사이클이 발생하는 것은 역방향 간선이 생기는 것이다.
# dfs spanning tree에서 정방향, 역방향, 크로스엣지를 다시 한 번 살펴보자
# union-find를 활용한 위상 정렬을 다시 한 번 살펴보는 것이 좋을 것 같다.


import sys
def input(): return sys.stdin.readline().rstrip()


def dfs(here):
    global possible
    visited[here] = 1
    if not possible:
        return
    for nxt in graph[here]:
        if not visited[nxt]:
            dfs(nxt)
        if not finished[nxt]:
            possible = False
            return
    finished[here] = 1
    stack.append(here)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
finished = [0] * (n+1)
stack = []
possible = True

for _ in range(m):
    nums = list(map(int, input().split()))
    for i in range(1, nums[0]):
        graph[nums[i]].append(nums[i+1])

for v in range(1, n+1):
    if not visited[v]:
        dfs(v)

if not possible:
    print(0)
else:
    stack.reverse()  # 아마 이게 시간 복잡도가 더 적을 것 같다.
    for v in stack:
        print(v)
