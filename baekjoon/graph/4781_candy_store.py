# 굳이 여러개 살 수 있다고 해서 여러 개를 구입할 필요는 없겠구나
# 예를 들어
# 2 8.00
# 700 7.00
# 199 2.00
# dp[398] = dp[199] + 2.00 이므로 dp[398] = 4.00이 자동으로 된다.
# 진짜 dp를 제대로 이해하지도 못했네...
# 부동 소수점 오류미쳤다... 이것 때문에 다 날라갔네

import sys
input = lambda : sys.stdin.readline()

while True:
    n,m = input().split()
    n,m = int(n), int(float(m)*100 + 0.5)
    if n == 0 and m == 0:
        break
    candy = []
    for _ in range(n):
        a,b = input().split()
        a,b = int(a), int(float(b) * 100 + 0.5)
        candy.append((b,a))
    candy.sort()
    dp = [0] * 10001
    for i in range(n):
        for j in range(m+1):
            if j >= candy[i][0]:
                dp[j] = max(dp[j-candy[i][0]] + candy[i][1],dp[j])
    print(dp[m])