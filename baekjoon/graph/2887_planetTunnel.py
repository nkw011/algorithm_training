# 문제에서 정의된 거리구하기를 이용해서 모든 노드끼리의 거리를 구하지 않아도 되는 식으로 푼다.
# 가장 기본적인 방법은 O(100000^2)이기 때문에 메모리초과가 나온다.
# 따라서 1 ~ n까지 거리를 다 구할 필요 없이 인근 노드끼리의 거리만 계산하는 방식으로 구한다.
# 인근 거리는 x,y,z 모두 3가지가 나오기 때문에 3가지를 이용해서 구하였다.

import sys
def input(): return sys.stdin.readline().rstrip()


def findParent(a):
    if parent[a] != a:
        parent[a] = findParent(parent[a])
    return parent[a]


def union(a, b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal():
    ret = 0
    for c, a, b in edges:
        if findParent(a) != findParent(b):
            union(a, b)
            ret += c
    return ret


n = int(input())
loc = []
edges = []
x, y, z = [], [], []

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    edges.append((abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]))
    edges.append((abs(z[i][0]-z[i+1][0]), z[i][1], z[i+1][1]))
edges.sort()

parent = [i for i in range(n)]

print(kruskal())
