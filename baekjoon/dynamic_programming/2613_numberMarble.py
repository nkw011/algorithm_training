# 뭔가 문제 요구 조건만 잘 고려해서 풀면 풀 수 있었던 문제였었다.
# 다행히 요구조건 빠짐없이 잘 했던 것 같다.

# 요구조건을 빠짐없이

import sys
INF = int(1e5)
def input(): return sys.stdin.readline().rstrip()


def find(i, num):
    if num == 0:
        return pSum[n-1] - pSum[i-1]
    if i == n:
        if num > 0:
            return INF
        return 0
    if dp[i][num] != -1:
        return dp[i][num]
    dp[i][num] = INF
    for k in range(i+1, n):
        temp = find(k, num-1)
        if temp != INF or temp != -1:
            if dp[i][num] > max(pSum[k-1]-pSum[i-1], temp):
                dp[i][num] = max(pSum[k-1]-pSum[i-1], temp)
                parent[i][num] = k
    return dp[i][num]


n, m = map(int, input().split())
marble = list(map(int, input().split()))
pSum = [0] * n
pSum[0] = marble[0]
parent = [i for i in range(n)]

for i in range(1, n):
    pSum[i] = marble[i] + pSum[i-1]

dp = [[-1] * m for _ in range(n)]
parent = [[n] * m for _ in range(n)]

result = INF
for k in range(1, n):
    temp = find(k, m-2)
    if temp != INF or temp != -1:
        if result > max(pSum[k-1], temp):
            result = max(pSum[k-1], temp)
            parent[0][m-1] = k

cnt = m-1
i = 0
s = 0
print(result)
while cnt > 0:
    s += (parent[i][cnt] - i)
    print(parent[i][cnt]-i, end=' ')
    i = parent[i][cnt]
    cnt -= 1
print(n-s)
