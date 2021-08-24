# 입력으로 알파벳이 들어오는 게 아니라 0이 들어오는 것을 catch하지 못했다.
# 전형적인 minimum spanning tree 찾는 알고리즘이었다.

import sys
def input(): return sys.stdin.readline().rstrip()

def findParent(a):
    if parent[a] != a:
        parent[a] = findParent(parent[a])
    return parent[a]

def union(a,b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def convert(alpha):
    if ord('a') <= ord(alpha) <= ord('z'):
        return ord(alpha) - ord('a') +1
    elif ord('A') <= ord(alpha) <= ord('Z'):
        return ord(alpha) - ord('A') + 27
    else :
        return 0

def kruskal():
    ret = 0
    count = 0
    for cost, a,b in edges:
        if findParent(a) != findParent(b):
            union(a,b)
            count += 1
            ret += cost
    for i in range(n):
        for j in range(i+1,n):
            if findParent(i) != findParent(j):
                return -1
    return ret

n = int(input())
parent = [i for i in range(n)]
nums = [list(map(convert,input())) for _ in range(n)]
edges = []
total = 0

for i in range(n):
    for j in range(n):
        if nums[i][j] == 0: continue
        edges.append((nums[i][j],i,j))
        total += nums[i][j]
        
edges.sort()
ret = kruskal()

if ret != -1:
    print(total - ret)
else:
    print(-1)