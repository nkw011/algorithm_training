# 해설: https://nkw011.github.io/programmers/programmers-12914/

def solution(n):
    dp = [0] * (n+1)
    for i in range(1,n+1):
        if i == 1: dp[i] = 1
        elif i == 2: dp[i] = 2
        else: dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]
