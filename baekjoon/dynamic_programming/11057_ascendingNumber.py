import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [[1] * 10]

for i in range(1,n):
    dp.append([0]*10)
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])%10007
        
print(sum(dp[n-1]) % 10007)