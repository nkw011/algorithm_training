import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = [0] * 10001

for _ in range(n):
    nn = int(input().rstrip())
    nums[nn] += 1
    
count = 0
for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            sys.stdout.write("{}\n".format(i))