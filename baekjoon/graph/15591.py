### 문제 제한:  512000KB   2000ms
### 첫번째 풀이: 449776KB	3484ms
### 두번째 풀이: 124220KB	1252ms
# 첫번째 방식: 특정 동영상에서 모든 동영상에 대해 유사도를 구한뒤 그 중 K 이상인 동영상의 갯수를 구함.
# 두번째 방식: USADO를 그 경로의 모든 연결들의 USADO 중 최솟값으로 정의했기 때문에 탐색시 유사도가 K이상인 것만 탐색하여 시간 절약
#           (경로 중 K미만인 것이 나오면 탐색을 더이상 진행하지 않음)

######### 두번째 풀이 ############
import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def bfs(s,k):
    visited = [0] * (n+1)
    visited[s] = 1
    q = deque([s])
    while q:
        w = q.popleft()
        for nxt, c in graph[w]:
            if not visited[nxt] and c >= k:
                visited[nxt] = 1
                q.append(nxt)
    return sum(visited) - 1

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    p,q,r = map(int,input().split())
    graph[p].append((q,r))
    graph[q].append((p,r))
    
for _ in range(m):
    k,v = map(int,input().split())
    print(bfs(v,k))




########## 첫번째 풀이 ############
import sys
from collections import deque
INF = 1e13
def input(): return sys.stdin.readline().rstrip()

def bfs(s,k):
    q = deque()
    dist[s][s] = 0
    for nxt in graph[s]:
        q.append(nxt)
    while q:
        w = q.popleft()
        for nxt in graph[w]:
            min_d = min(dist[s][w], dist[w][nxt])
            if dist[s][nxt] == INF and dist[s][nxt] > min_d:
                dist[s][nxt] = min_d
                q.append(nxt)
    cnt = 0
    for i in range(1,n+1):
        if dist[s][i] != INF and dist[s][i] >= k:
            cnt += 1
    return cnt

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
dist = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(n-1):
    p,q,r = map(int,input().split())
    graph[p].append(q)
    graph[q].append(p)
    dist[p][q] = r
    dist[q][p] = r
    
for _ in range(m):
    k,v = map(int,input().split())
    print(bfs(v,k))
