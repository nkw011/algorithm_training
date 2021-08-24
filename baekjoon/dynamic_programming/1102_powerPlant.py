# 애초에 함수 설계가 잘못되어있던 문제였다.
# 문제를 잘못 이해하고 한 타임에 한 발전소만을 이용해서 푼다는 것 자체가 잘못되었던 것 같다.
# 앞으로는 이런 실수를 줄이고 문제의 <조건> 과 <요구사항>이 뭔지 정확히 분석해서 결과를 도출해야겠다.

import sys
INF = int(1e4)
def input(): return sys.stdin.readline().rstrip()


def fixAll(survived):
    count = 0
    for i in range(n):
        if survived & (1 << i):
            count += 1
    return count >= p


def fix(i, survived):
    # 아마 여기 fixAll()이 아니라 i >= p 이 조건을 달면 더 좋았을 것 같다.
    if fixAll(survived):
        return 0
    if dp[i][survived] != -1:
        return dp[i][survived]
    dp[i][survived] = INF
    for k in range(n):
        if survived & (1 << k):
            for nxt in range(n):
                if survived & (1 << nxt):
                    continue
                dp[i][survived] = min(
                    dp[i][survived], cost[k][nxt]+fix(i+1, survived | (1 << nxt)))
    return dp[i][survived]


n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n+1)]
now = list(input())
p = int(input())
check = 0
count = 0
for i in range(n):
    if now[i] == 'Y':
        check += (1 << i)
        count += 1

result = fix(count, check)
if result == INF:
    print(-1)
else:
    print(result)
