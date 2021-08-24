import sys
input = lambda : sys.stdin.readline().rstrip()

def findParent(a):
    if parent[a] == -1: return parent[a]
    if parent[a] != a:
        parent[a] = findParent(parent[a])
    return parent[a]

def union(a,b):
    a = findParent(a)
    b = findParent(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

def kruskal():
    ret = 0
    for cost, a, b in edges:
        if findParent(a) != findParent(b):
            ret += cost
            union(a,b)
    return ret

n,m,k = map(int,input().split())
plant = list(map(int,input().split()))
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()
parent = [ i for i in range(n+1)]
for w in plant:
    parent[w] = -1
    
print(kruskal())