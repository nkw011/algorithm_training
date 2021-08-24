import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = [int(input().rstrip()) for _ in range(n)]
dp = [[number,1] for number in array]

for i in range(1,n):
    # 나는 가장 작은 케이스를 실수했다... 가장 작을 때는 어떻게 될지를 먼저 생각해보고 하자...
    # 기왕이면 선택한다.. 선택하지 않는다.. 등등의 케이스를 잘 나누도록 하자
    if i == 1 :
        dp[i][0] = array[i] + array[i-1]
        dp[i][1] = 2
    elif i == 2 :
        dp[i][0] = max(array[i] + array[i-2],array[i-1] + array[i])
        if dp[i][0] == array[i-1] + array[i]:
            dp[i][1] = 2
    else:
        if dp[i][0] < dp[i-2][0] + array[i]:
                dp[i][0] = dp[i-2][0] + array[i]
                dp[i][1] = 1
        if dp[i-1][1] <2 :
            if dp[i][0] < dp[i-1][0] + array[i]:
                dp[i][0] = dp[i-1][0] + array[i]
                dp[i][1] = 2
        dp[i][0] = max(dp[i][0],dp[i-1][0])
        
for number in dp:
    print(number[0],end=" ")
print()
print(dp[n-1][0])