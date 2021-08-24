import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int,input().split()))
nums.sort()
numdict = {}
for i in range(n):
    numdict[nums[i]] = i
for num in nums:
    print(numdict[num],end=" ")
print()