import sys
def input(): return sys.stdin.readline().rstrip()

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n+1)]
edges = [(int(input()), 0, i+1) for i in range(n)]
dist = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            edges.append((dist[i][j], i+1, j+1))
edges.sort()
result = 0
for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent,a,b)
        result += c
print(result)
