# 모자 쓰기 문제와 같은 거라고 하네...
# 조합론 문제 다시 풀어봐야겠다.

import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
    if i == 2:
        dp[i] = 1
    else:
        dp[i] = (i-1)*(dp[i-2] + dp[i-1])
        dp[i] %= 1000000000

print(dp[n])
