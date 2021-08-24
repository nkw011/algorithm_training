import sys
input = sys.stdin.readline 

def findParent(a):
    if parent[a] != a:
        parent[a] = findParent(parent[a])
    return parent[a]

def union(a,b):
    a = findParent(a)
    b = findParent(b)
    if a < b : parent[b] = a
    else : parent[a] = b


n = int(input().rstrip())
m = int(input().rstrip())
result = 0
edges = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

for cost,a,b in edges:
    if findParent(a) != findParent(b):
        union(a,b)
        result += cost
print(result)