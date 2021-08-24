import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)

def findParent(x):
    if parent[x] != x:
        parent[x] = findParent(parent[x])
    return parent[x]

def union(a,b):
    pa = findParent(a)
    pb = findParent(b)
    if pa < pb:
        parent[pb] = pa
    else :
        parent[pa] = pb

n,m = map(int,input().split())
parent = [i for i in range(n)]
isCycle = False
result = 0
for count in range(1,m+1):
    a,b = map(int,input().split())
    # not isCycle을 달지 않으면 cylce이 나올 때마다 result 값이 갱신이 된다.
    if not isCycle and findParent(a) == findParent(b):
        isCycle = True
        result = count
    else :
        union(a,b)
print(result)