import sys
input = sys.stdin.readline

n= int(input().rstrip())
cards = list(map(int,input().split()))
dp = [0] * (n+1)
dp[1:] = cards[:]

for i in range(1,n+1):
    for j in range(i):
        dp[i] = min(dp[i],dp[i-j]+dp[j])
        
print(dp[n])