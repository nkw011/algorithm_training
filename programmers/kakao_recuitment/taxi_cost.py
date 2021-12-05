# https://programmers.co.kr/learn/courses/30/lessons/72413

# 해결방안
# 1. 각 지점에서 주어진 도착지점까지 가는 최단거리를 알아보고
# 2. (출발 지점 ~ 중간 지점 + 중간지점 ~ 도착지점 A + 중간지점 ~ 도착지점 B)의 합이 가장 작은 것을 반환한다.
# 3. n이 200이므로 floyd-warshall을 이용한다.

def solution(n,s,a,b,fares):
    INF = 1e10
    taxi = [[INF] * (n+1) for _ in range(n+1)]
    for c,d,f in fares:
        taxi[c][d] = f
        taxi[d][c] = f
    for node in range(1,n+1):
        taxi[node][node] = 0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                taxi[i][j] = min(taxi[i][j],taxi[i][k] + taxi[k][j]) # 이 부분에서 오래 걸리는 것 같다.
    cost = [taxi[s][node] + taxi[node][a] + taxi[node][b] for node in range(1,n+1)]
    return min(cost)
