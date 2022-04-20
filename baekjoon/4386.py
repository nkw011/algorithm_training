# 해설: https://nkw011.github.io/baekjoon/baekjoon-4386/

import sys
def input(): return sys.stdin.readline().rstrip()

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
node = { i:tuple(map(float, input().split())) for i in range(n)} 
parent = [i for i in range(n)]
edges = []
for i in range(n):
    x1,y1 = node[i]
    for j in range(i+1,n):
        x2,y2 = node[j]
        dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        edges.append((i,j,dist))
edges.sort(key=lambda x: x[2])
result = 0
for a, b, cost in edges:
    parent_a, parent_b = find_parent(a), find_parent(b)
    if parent_a != parent_b:
        result += cost
        union(a,b)
print(result)
