# 10일 때 정답은 1이 나와야하는데 2가 나와서 100%에서 틀렸다.
# 따라서 0일 때는 정답이 도출되지 않아야하므로 dp[n-1][1:] 즉 1이상일 때만 합을 구하니 정답이 되었다.
# 사실 이걸 한 줄로 써도 될 것 같긴하다...

import sys
input = lambda : sys.stdin.readline()

nums = list(map(int,input().rstrip()))
n = len(nums)
dp = [[0] * 35 for _ in range(n)]
dp[0][nums[0]] = 1

for i in range(1,n):
    for j in range(1,35):
        if dp[i-1][j] > 0:
            dp[i][nums[i]] += dp[i-1][j]
            if j * 10 + nums[i] <= 34:
                dp[i][j*10+nums[i]] += dp[i-1][j]
print(sum(dp[n-1][1:]))