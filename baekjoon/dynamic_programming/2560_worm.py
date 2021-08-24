# 이런식으로 담백하게 생각하면 좋을텐데....
# 결국 어제 날짜를 합친다는게 a~b-1까지의 합을 계속해서 누적해서 더한다는 것을 알았어야했는데...
# 왜 나는 이걸 몰랐을까...
# 과연 계속 깨달았을까?

import sys
def input(): return sys.stdin.readline().rstrip()

a,b,d,n = map(int,input().split())
dp = [0] * (n+1)
dp[0] = 1

for i in range(1,n+1):
    dp[i] = dp[i-1]
    if i-a >= 0:
        dp[i] += dp[i-a]
    if i-b >=0:
        dp[i] -= dp[i-b]
    dp[i] %= 1000

if n >= d:
    print((dp[n]-dp[n-d]) % 1000)
else:
    print(dp[n] % 1000)