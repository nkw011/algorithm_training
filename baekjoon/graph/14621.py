# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-14621
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-14621/

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

n, m = map(int, input().split())
school = ['-1']+ list(input().split())
parent = [ i for i in range(n+1)]
edges = [ tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
result, cnt = 0,0
for a, b, c in edges:
    if school[a] == school[b]: continue
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
        cnt += 1
if cnt == n-1:
    print(result)
else:
    print(-1)
