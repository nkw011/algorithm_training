import bisect
import sys
input = sys.stdin.readline
INF = 1001

n = int(input().rstrip())
inputs = list(map(int,input().split()))
inputs.reverse()

dp = [0] * (n+1)
array = [INF] * (n+1)
array[0] = 0
count = 1
for i in range(n):
    index = bisect.bisect_left(array,inputs[i])
    array[index] = inputs[i]
    if index == count:
        dp[index] = count -1
        count += 1

print(count-1)