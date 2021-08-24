# 처음 시도했던 코드는 각 노드별로 자식인 노드를 모두 담으려고 했기 때문에 메모리 초과가 일어났다.
# 두번째로 시도한 코드는 score가 새로 나올 때마다 계속 자손노드까지 탐색해서 score를 갱신하려고해서 시간초과가 일어났다. (즉 한번 나올때마다 그래프를 전체 탐색함)
# 세번째로는 dp랑 graph 탐색을 활용해서 풀었다... 
# 일단 dp는 한 번 값이 정해지면 더이상 값의 변동이 없어야한다. 
# 그래프에는 다음 자식 노드만을 담았다.
# score를 입력하고 루트부터 시작해서 그래프를 탐색하였다, 이 때 score 값이 0이 아닌 경우 그 다음 자식노드의 score 값을 갱신해주었다.
# 노드에  방문해서 다음 자식 노드의 score 값을 갱신할 때는 그 노드의 score 값이 이미 확정적으로 되었기 때문에 (부모를 방문한 상태라 더이상 값이 변할 수 없음)
# dp를 이용해서 문제를 풀 수 있었다. 이렇게 전체 노드를 탐색하면 두번째 방법과는 달리 탐색 한 번만으로 전체 노드의 score 값을 갱신해줄 수 있었다.

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
parent = list(map(int,input().split()))
newParent = [0]

# 다만 이 부분이 조금 아쉽다. extend를 사용하지 않았으면 메모리로나 시간으로나 더 줄일 수 있었을 것 같다.
newParent.extend(parent)
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    pa = newParent[i]
    # 자식의 자손 노드까지 갱신하는 것이 아닌 바로 다음 자식 노드만을 그래프에 추가하는 방식으로 하였다.
    # 따라서 마지막 score 값을 갱신할 때 루트부터 차례대로 노드를 방문하면서 다음 자식노드의 score 값을 갱신하였다.
    if pa != -1:
        graph[pa].append(i)

score = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    score[a] += b

# 루트부터 그래프를 탐색하면서 자식 노드의 score값을 갱신하였다.
# 어떤 노드를 방문할 때 이미 그 노드의 부모 노드를 방문을 완료한 상태이므로 그 노드의 score 값은 확정적인 것이 된다.
# 따라서 dp를 사용해서 문제를 풀 수 있었다. 또한 그래프를 1번만 탐색하면서 문제를 풀 수 있어서 시간초과가 일어나지 않았다.
for i in range(1,n+1):
    if score[i] > 0:
        for nxt in graph[i]:
            score[nxt] += score[i]

for num in score[1:]:
    print(num,end=" ")
print()