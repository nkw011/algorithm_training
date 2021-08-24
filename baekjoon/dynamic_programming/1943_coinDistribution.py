# 배낭 채우기 문제를 응용하면 될 것 같다.
# 주의해서 해당 금액이 1이면 천천히 낼 수 있는 금액을 정하면 될 것 같다.

import sys
def input(): return sys.stdin.readline().rstrip()

def findCoin(i,total):
    if i == 0:
        if dp[i][total] == -1:
            return 0
        return 1
    if dp[i][total] != -1: return dp[i][total]
    dp[i][total] = 0
    for cnt in range(coin[i][1]+1):
        if total >= cnt * coin[i][0] and findCoin(i-1,total-cnt*coin[i][0]):
            dp[i][total] = 1
    return dp[i][total]


for _ in range(3):
    n = int(input())
    total = 0
    coin = []
    for _ in range(n):
        a,b = map(int,input().split())
        coin.append((a,b))
        total += a*b
    coin.sort(key=lambda x:x[0])
    dp = [[-1] * (total+1) for _ in range(n+1)]
    for cnt in range(coin[0][1]+1):
        dp[0][coin[0][0] * cnt] = 1
    if total % 2 != 0:
        print(0)
        continue
    print(findCoin(n-1,total//2))