import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split()))
nums.sort(key=lambda x: abs(x))

o1, o2 = 1e14, 1e14
for i, num in enumerate(nums[:-1]):
    if abs(o1 + o2) > abs(num + nums[i+1]):
        o1, o2 = num, nums[i+1]

print(*sorted([o1, o2]))