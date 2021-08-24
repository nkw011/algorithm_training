# 아무 값이 안들어갔을 때는 1로 만들어주어야한다... LIS 기본인데... (처음을 0으로 놓고 시작하는 게 맘이 편할 것 같다.)

import sys
input = sys.stdin.readline

n = int(input().rstrip())
boxes = list(map(int,input().split()))
dp = [0] * n
dp[0] = 1

for i in range(1,n):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[j] +1, dp[i])
    if dp[i] == 0:
        dp[i] = 1

print(max(dp))