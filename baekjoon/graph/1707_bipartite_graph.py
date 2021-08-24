import sys
input = sys.stdin.readline
from collections import deque

def isBigraph(graph,start): 
    q = deque()
    q.append(start)
    color[start] = 1
    while q:
        w = q.popleft()
        for nxt in graph[w]:
            if color[nxt] == 0:
                color[nxt] = color[w] * (-1)
                q.append(nxt)
            else :
                if color[nxt] == color[w]:
                    return False
    return True
     
T = int(input().rstrip())
for loop in range(T):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    color = [0] * (v+1)
    
    # 모든 경로를 탐색해야하기 때문에 아마도 양방향 그래프로 만든 것 같다.
    # start가 모든 노드와 연결된 것이 아니기 때문에 모든 노드에 출발해야하지만 이미 색깔이 정해져있는 곳은 다시 방문하지 않아도 된다.
    # 새로 방문을 시작하는 곳이 처음과 똑같은 것(1)은 연결되지 않고 새로 시작한다는 뜻은 시작 부분(1)과 연결된 것(-1)의 색깔과 정반대(1)이기 때문이다.
    # 그래프 탐색에 있어 중요한 깨달음을 얻는다 (특히 두번째 항목과 방문처리 같은 것들...)
    for _  in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    possible = True
    for i in range(1,v+1):
        if color[i] == 0 and not isBigraph(graph,i):
            print("NO")
            possible = False
            break
    if possible:
        print("YES")