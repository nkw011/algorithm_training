# 조합 탐색에서 지금 선택하지 않는 것은 이전 것을 택하는 것과 같다.
# 내 풀이에 대한 확신이 없어서 계속 주저하게 되는 것 같다.

import sys
def input(): return sys.stdin.readline().rstrip()


n, s = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
picture.sort()
top = [-1] * n
dp = [0] * n

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if picture[i][0] - picture[j][0] >= s:
            top[i] = j
            break


dp[0] = picture[0][1]
for i in range(1, n):
    dp[i] = max(dp[i-1], picture[i][1])
    if top[i] != -1:
        dp[i] = max(dp[i], dp[top[i]] + picture[i][1])


print(dp[n-1])
