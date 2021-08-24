import sys
MOD = 1000000009
def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())

if k < 3 or n <= 4:
    print(k**n % MOD)
else:
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] * k
        if i-5 >= 0:
            dp[i] -= (dp[i-5] * 2)
        # 중복되는 것을 처라하여보았다.
        if i-7 >= 0:
            dp[i] += dp[i-7]
        dp[i] %= MOD
    print(dp[n])
