# https://programmers.co.kr/learn/courses/30/lessons/12978
# N <= 50 이라서 Floyd-Warshall을 적용하였다.

def solution(N, road, K):
    INF = (5e5 * 2e3) +1
    graph = [[INF] * (N+1) for _ in range(N+1)]
    for a,b,c in road:
        graph[a][b] = min(graph[a][b],c)
        graph[b][a] = min(graph[b][a],c)
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    answer = 1
    for i in range(2,N+1):
        if graph[1][i] <= K:
            answer += 1

    return answer
