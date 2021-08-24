import sys
input = lambda : sys.stdin.readline().rstrip()

def findParent(a):
    if parent[a] != a:
        parent[a] = findParent(parent[a])
    return parent[a]

def union(a,b):
    a = findParent(a)
    b = findParent(b)
    if price[a] < price[b]:
        parent[b] = a
    else :
        parent[a] = b

n,m,k = map(int,input().split())
price = list(map(int,input().split()))
parent = [i for i in range(n)]

for _ in range(m):
    x,y = map(int,input().split())
    if findParent(x-1) != findParent(y-1):
        union(x-1,y-1)
result = 0
for i in range(n):
    if parent[i] == i:
        result += price[i]
if result <= k:
    print(result)
else :
    print("Oh no")