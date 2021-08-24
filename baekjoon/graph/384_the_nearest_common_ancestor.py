# 두 노드의 공통 조상을 찾기 위해 먼저 a의 조상 노드를 모두 표시하고
# b의 조상 노드가 표시된 조상 노드를 만나면 바로 출력 후 종료한다. (담백하네)

import sys
input = lambda : sys.stdin.readline().rstrip()


T = int(input())
while T:
    n = int(input())
    parent = [i for i in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        parent[b] = a
    x,y = map(int,input().split())
    pa,pb = [x],[y]
    while parent[x] != x:
        pa.append(parent[x])
        x = parent[x]
    while parent[y] != y:
        pb.append(parent[y])
        y = parent[y]
    for n1 in pa:
        possible = False
        for n2 in pb:
            if n1 == n2:
                print(n1)
                possible = True
                break
        if possible:
            break
    T -= 1