import sys
input = sys.stdin.readline

def findMax(array,length):
    dp = [0] * length
    dp[0] = 1
    for i in range(1,n):
        if array[i] >= array[i-1]:
            dp[i] = dp[i-1] +1
        else :
            dp[i] = 1
    return max(dp)

n = int(input().rstrip())

inputs = list(map(int,input().split()))
result1 = findMax(inputs,n)
inputs.reverse()
result2 = findMax(inputs,n)
print(max(result1,result2))