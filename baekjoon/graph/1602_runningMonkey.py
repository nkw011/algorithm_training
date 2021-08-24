# 최단 경로 구하는 것일 때 n이 작으면 floyd-warshall을 먼저 떠올려보자

# 그런데 이렇게 풀었어야했을까?
# 1) 만약 k가 제일 크지 않을 경우: 어차피 경로상 최대 cost를 합하고 k가 i,j 경로상에 있기 때문에 maxcost(k,i,j) 를 이용한다.
#    거리는 dist1[i][j] = min(dist1[i][j], dist1[i][k] + dist1[k][j])의 결과값인 min(dist1[i][j])를 쓰면 된다.
# 2) 제일 큰 경우: 이 때는 무조건 이 경로를 이용하기 때문에(dist1[i][k] + dist1[k][j]) + cost(k)를 합해서 기존 값하고 어떤 것이 작은 지 비교하면 된다.
#                 뭔가 조건 하나를 빼먹었지만 통과가 되었다..
#                 바로 k를 통해 지나가지 않는 경우를 check를 해서 통과하여야했다. (일단 문제는 알았고 맞았으니 넘어가자)

import sys
INF = int(1e11)
def input(): return sys.stdin.readline().rstrip()


n, m, q = map(int, input().split())
temp = list(map(int, input().split()))

city = []
for i in range(1, n+1):
    city.append((temp[i-1], i))
city.sort()

dist1 = [[INF] * (n+1) for _ in range(n+1)]
dist2 = [[INF] * (n+1) for _ in range(n+1)]

# 이 부분은 floyd-warshall에서
for i in range(1, n+1):
    dist1[i][i] = 0


for _ in range(m):
    a, b, c = map(int, input().split())
    dist1[a][b] = c
    dist1[b][a] = c

# 내가 의심이 가는 부분이 있어 진행이 안되는 경우 의심가는 부분을 가정하고 해결해나가면 된다.

# 그런데 이렇게 풀었어야했을까?
# 1) 만약 k가 제일 크지 않을 경우: 어차피 경로상 최대 cost를 합하고 k가 i,j 경로상에 있기 때문에 maxcost(k,i,j) 를 이용한다.
#    거리는 dist1[i][j] = min(dist1[i][j], dist1[i][k] + dist1[k][j])의 결과값인 dist1[i][j]를 쓰면 된다.
# 2) 제일 큰 경우: 이 때는 무조건 이 경로를 이용하기 때문에(dist1[i][k] + dist1[k][j]) + cost(k)를 합해서 기존 값하고 어떤 것이 작은 지 비교하면 된다.

# floyd-warshall
for idx in range(n):
    cost = city[idx][0]
    k = city[idx][1]
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist1[i][j] = min(dist1[i][j], dist1[i][k] + dist1[k][j])
            if cost <= temp[i-1] or cost <= temp[j-1]:
                dist2[i][j] = min(dist2[i][j], dist1[i][j] +
                                  max(temp[i-1], temp[j-1]))
            else:
                dist2[i][j] = min(dist2[i][j], dist1[i]
                                  [k] + dist1[k][j] + cost)

for _ in range(q):
    a, b = map(int, input().split())
    if dist2[a][b] != INF:
        print(dist2[a][b])
    else:
        print(-1)
