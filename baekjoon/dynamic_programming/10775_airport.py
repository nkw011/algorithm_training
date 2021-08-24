# 그 이전 것과 결합하는 이유는
# 이번 게이트와는 결합을 하지 못하기 때문에
# 그 이전 게이트로 가라는 뜻과 같다.
# 따라서 이런 방식으로 O(1)만에 어디에 도킹을 해야되는지 알 수 있다.
# disjoint-set 및 union-find의 활용을 그래프 말고 다른 곳에서 할 수도 있다는 것을 알았다.


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


n = int(input())
m = int(input())
airplane = [int(input()) for _ in range(m)]
parent = [i for i in range(n+1)]

count = 0
for gate in airplane:
    p = findParent(gate)
    if p == 0:
        break
    union(p, p-1)
    count += 1

print(count)
