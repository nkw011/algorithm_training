import sys
input = lambda : sys.stdin.readline()
sys.setrecursionlimit(100000)

def denoteParent(start,end):
    if start == end:
        return 1
    node = parent[start]
    finished[start] = 1
    count = 1
    while node != end:
        finished[node] = 1
        count += 1
        node = parent[node]
    finished[node] = 1
    count += 1
    return count

def dfs(node):
    global remain
    nxt = graph[node]
    if not visited[nxt]:
        visited[nxt] = 1
        parent[nxt] = node
        dfs(nxt)
    elif visited[nxt] and not finished[nxt] :
        remain -= denoteParent(node,nxt)
    finished[node] = 1

T= int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    graph = list(map(int,input().split()))
    graph.insert(0,0)
    visited = [0] * (n+1)
    finished = [0] * (n+1)
    parent = [0] * (n+1)
    remain = n
    for i in range(1,n+1):
        if not finished[i]:
            visited[i] = 1
            dfs(i)
    print(remain)