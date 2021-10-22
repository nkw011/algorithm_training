# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    adj = [[0] * (n+1) for _ in range(n+1)]
    for a, b in results:
        adj[a][b] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                adj[i][j] = adj[i][j] or (adj[i][k] and adj[k][j])

    ret = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if adj[i][j] or adj[j][i]:
                cnt += 1
        if cnt == n-1:
            ret += 1
    return ret
