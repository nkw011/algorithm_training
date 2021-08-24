import sys
input = lambda : sys.stdin.readline().rstrip()

n,m = map(int,input().split())
mem = list(map(int,input().split()))
c = list(map(int,input().split()))
leng = sum(c)
dp = [[-1] * (leng+1) for _ in range(n)]

for i in range(n):
    for j in range(leng+1):
        dp[i][j] = 0
        if i >=1:
            dp[i][j] = dp[i-1][j]
            if j >= c[i]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-c[i]]+mem[i])
        else :
            if j >= c[i]:
                dp[i][j] = mem[i]
result = leng
for cost in range(leng+1):
    for i in range(n):
        if dp[i][cost] >= m:
            result = cost
            break
    if result != leng:
        break
print(result)