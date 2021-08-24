# 조합은 조합으로 순열은 순열로 구분해서 문제를 풀도록 하자...

import sys
input = sys.stdin.readline
INF = 2500

def dfs(select,count,last,result):
    global minValue
    if select == count:
        total = 0
        for i in range(h):
            each = 2500
            for j in range(count):
                each = min(each,distances[i][result[j]])
            total += each
        minValue = min(minValue,total)
        return
    # 조합 문제인데 계속 순열로 풀어서 시간 초과가 났었다....
    # 조합은 조합으로 풀자..
    for index in range(last+1,c):
        if not visited[index]:
            visited[index] = 1
            result.append(index)
            dfs(select+1,count,index,result)
            result.pop()
            visited[index] = 0

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 :
            houses.append((i,j))
        elif matrix[i][j] == 2:
            chickens.append((i,j))

h,c = len(houses), len(chickens)
visited = [0] * c
distances = [[INF] * c for _ in range(h)]
for i in range(h):
    for j in range(c):
        distances[i][j] = abs(houses[i][0] - chickens[j][0]) + abs(houses[i][1] - chickens[j][1])

minValue = 2500
dfs(0,m,-1,[])
print(minValue)