# 피보나치의 음수로의 확장은 n이 짝수 * (-1) 인 경우에만 기존 피보나치에서 -1을 곱한 것이다.
# f(-1) == f(1) / f(-2) == f(2) * (-1) / f(-3) == f(3) / f(-4) == f(4) * (-1) ... 

import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0] * 1000001
dp[0] = 0
dp[1] = 1
for i in range(2,abs(n)+1):
    dp[i] = dp[i-2] + dp[i-1]
    dp[i] %= 1000000000
    
if n < 0 and n*(-1) % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else :
    print(1)
print(dp[abs(n)] % 1000000000)