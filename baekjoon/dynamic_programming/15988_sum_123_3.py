import sys
input = sys.stdin.readline

T = int(input().rstrip())
numberList = []
for _ in range(T):
    numberList.append(int(input().rstrip()))
# 정렬한 답을 내놓으면 안된다...
# numberList..sort()

dp = [0] * (1000001)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
        
for num in numberList:
    print(dp[num])