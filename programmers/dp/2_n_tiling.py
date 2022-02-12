# https://programmers.co.kr/learn/courses/30/lessons/12900
# DP에서 유명한 n-tiling 문제이다.

def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] += dp[i-1] 
        if i-2 >= 0:
            dp[i] += dp[i-2]
        dp[i] %= 1000000007
    return dp[n]
