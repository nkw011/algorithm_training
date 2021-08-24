import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v,e = map(int,input().split())
edges = []
parent = [i for i in range(v+1)]
result = 0

for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
    
edges.sort()
    
for cost,a,b in edges:
    if find_parent(a) != find_parent(b):
        union(a,b)
        result += cost
print(result)