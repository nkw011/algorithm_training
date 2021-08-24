import sys
input = sys.stdin.readline

# 이번 문제에서는 추가 조건(연속으로 같은 숫자를 사용불가)로 인해 
# 마지막으로 오는 수가 1이면? 그 앞에 올 수 있는 숫자는 2 또는 3이 된다.
# 마지막으로 오는 수가 2이면? 그 앞에 올 수 있는 숫자는 1 또는 3이 된다.
# 마지막으로 오는 수가 3이면? 그 앞에 올 수 있는 숫자는 1 또는 2이 된다.
# 라는 규칙을 갖고 문제를 풀 것이다.
# 2차원 배열을 이용하면 간단하게 풀 수 있다.
# D[n][i] 는 마지막에 오는 수가 i일 때, 1,2,3의 합으로 정수 n을 만드는 경우의 수가 된다.

T = int(input().rstrip())
numberList = []
for _ in range(T):
    numberList.append(int(input().rstrip()))
maxValue = max(numberList)
dp = [[0,0,0],[1,0,0],[0,1,0],[1,1,1]]


for i in range(4,maxValue+1):
    dp.append([0,0,0])
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009
        
for num in numberList:
    print(sum(dp[num])%1000000009)