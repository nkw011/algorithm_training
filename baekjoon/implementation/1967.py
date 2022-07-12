# 풀이 및 해설: https://velog.io/@nkw011/baekjoon-1967

import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

def dfs(node):
    global result
    if not graph[node]: return 0
    ret = 0 # node가 부모노드인 서브 트리에서 node와 리프 노드 사이의 거리 중 최장 거리
    dist = [] # node가 부모노드인 서브 트리에서 node와 리프 노드 사이의 거리들을 담은 배열
    for nxt, c in graph[node]:
        if not visited[nxt]:
            visited[node] = 1
            nxt_d = dfs(nxt)
            dist.append(c+nxt_d)
            ret = max(ret, c+nxt_d)
    dist.sort() # 리프 노드들 사이의 거리 중 최장 거리가 해당 서브 트리의 지름이다. (트리 지름 후보)
    if len(dist) >= 2:
        result = max(result, dist[-2] + dist[-1])
    else:
        result = max(result, dist[-1])
    return ret

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

result = 0
visited = [0] * (n+1)
dfs(1)
print(result)
