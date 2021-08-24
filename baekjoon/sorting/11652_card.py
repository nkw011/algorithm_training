import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = {}
maxValue = 0
value = int(5e20)
for _ in range(n):
    num = int(input().rstrip())
    if num in nums.keys():
        nums[num] += 1
    else :
        nums[num] = 1
    if maxValue <= nums[num]:
        maxValue = nums[num]
        value = min(value,num)
print(value)