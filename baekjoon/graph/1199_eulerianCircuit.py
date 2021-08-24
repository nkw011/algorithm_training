# 1199_eulerianCircuit.py
# 왜 메모리 초과가 나오는지 잘 이해가 가지 않는다....
# python3로 바꿔서 제출하니 시간이 조금 오래걸리지만 메모리초과가 아니라서 성공

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(200000)

def makeGraph():
    for i in range(n):
        count = 0
        for j in range(n):
            if matrix[i][j] > 0:
                graph[i+1].append(j+1)
                count += matrix[i][j]
        if count % 2 == 1:
            return False
    return True

def eulerCircuit(here):
    for nxt in graph[here]:
        while matrix[here-1][nxt-1] > 0:
            matrix[here-1][nxt-1] -= 1
            matrix[nxt-1][here-1] -= 1
            eulerCircuit(nxt)
    print(here,end=' ')


n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
graph = [[] for _ in range(n+1)]
path = []

if makeGraph():
    eulerCircuit(1)
    print()
else :
    print(-1)