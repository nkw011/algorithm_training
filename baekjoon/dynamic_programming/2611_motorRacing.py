# 알고리즘은 문제 정의를 어떻게 하느냐에 따라 달려있다.
# 그리고 recurence relation이 어떤 동작으로 작동할까 미리 생각해봐야한다.
# 이걸 천천히 검증한 덕분에 문제를 해결할 수 있었던 것 같다.
# 앞으로 dp 문제를 풀 때 이런 방식으로 풀어야겠다.

# 위상정렬에 관한 문제라고도한다.

import sys
def input(): return sys.stdin.readline().rstrip()


def carRace(i):
    if i == 1:
        return 0
    if dp[i] != -1:
        return dp[i]
    dp[i] = 0
    for nxt in range(1, n+1):
        if dist[i][nxt] == 0:
            continue
        if dp[i] < dist[i][nxt] + carRace(nxt):
            dp[i] = dist[i][nxt] + carRace(nxt)
            parent[i] = nxt
    return dp[i]


n = int(input())
m = int(input())
dist = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c
dp = [-1] * (n+1)
parent = [i for i in range(n+1)]

for i in range(1, n+1):
    if dist[1][i] == 0:
        continue
    if dp[1] < dist[1][i] + carRace(i):
        dp[1] = dist[1][i] + carRace(i)
        parent[1] = i

print(dp[1])
v = parent[1]
print(1, end=' ')
while v != 1:
    print(v, end=' ')
    v = parent[v]
print(1)
