# 내가 생각한 분류: floyd-warshall, disjoint set
# 백준 내에서 분류: 강한 연결 요소 (strongly connected component)

import sys
def input(): return sys.stdin.readline().rstrip()


def findParent(a):
    if parent[a] != a:
        parent[a] = findParent(parent[a])
    return parent[a]


def union(a, b):
    a = findParent(a)
    b = findParent(b)
    if cost[a] < cost[b]:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
cost = list(map(int, input().split()))

connect = [list(map(int, input())) for _ in range(n)]
# i -> j로 갈 수 있는지 체크
for k in range(n):
    for i in range(n):
        for j in range(n):
            connect[i][j] = connect[i][j] or (connect[i][k] and connect[k][j])

# cost가 작은쪽으로 서로소 집합을 만들어서 최소한의 비용을 구한다.
# 결국 생각해보니까 police는 필요 없었다.
parent = [i for i in range(n)]
for i in range(n):
    for j in range(n):
        if connect[i][j] and connect[j][i]:
            union(i, j)

result = 0
for i in range(n):
    if parent[i] == i:
        result += cost[i]
print(result)
