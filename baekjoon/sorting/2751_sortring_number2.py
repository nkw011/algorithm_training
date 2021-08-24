import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(n)]
nums.sort()

for num in nums:
    print(num)