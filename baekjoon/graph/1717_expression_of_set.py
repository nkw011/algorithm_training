# 파이썬이 리스트 객체를 함수 인자로 전달할 때 어떤 방식으로 넘기는 지 살펴봐야겠다.
# parent 리스트를 함수 인자로 넘기지 않으면 '맞았습니다'이고 함수인자로 넘기게되면 '틀렸습니다'가 나오네...

import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)

# path-compression
def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

n,m = map(int,input().split())
parent = [i for i in range(n+1)] 
for _ in range(m):
    ex, k,l = map(int,input().split())
    if ex == 0:
        union(k,l)
    else :
        if find_parent(k) == find_parent(l):
            print("YES")
        else :
            print("NO")