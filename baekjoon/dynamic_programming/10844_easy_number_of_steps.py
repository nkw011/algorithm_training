import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp =[[0 for _ in range(10)]]
dp[0][1:] = [1] * 9

for i in range(1,n):
    dp.append([0] *10)
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9 :
            dp[i][j] += dp[i-1][j-1]
        else :
            dp[i][j] += dp[i-1][j+1]
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= 1000000000
# 합이 1000000000보다 커질 수 있음을 기억해서 나머지연산을 적용해야한다.
print(sum(dp[n-1])% 1000000000)