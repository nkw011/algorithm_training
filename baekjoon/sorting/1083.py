# 1, 각 숫자별로 몇 번을 움직여야 주어진 위치로 옮길 수 있는 지 체크
# 2. swap

import sys
def input(): return sys.stdin.readline().rstrip()


def swap(swap_i):
    while swap_i > 0:
        nums[swap_i], nums[swap_i-1] = nums[swap_i-1], nums[swap_i]
        swap_i -= 1


n = int(input())
nums = list(map(int, input().split()))
s = int(input())

# 첫번째 제출 풀이
answer = []
while s > 0:
    if not nums:
        break
    swap_i = 0
    for i, num in enumerate(nums):
        if i <= s and nums[swap_i] < num:
            swap_i = i
    s -= swap_i
    swap(swap_i)
    answer.append(nums[0])
    nums = nums[1:]
print(" ".join(map(str, answer + nums)))

# 두번째 제출 풀이
answer = []
while s > 0 and nums:
    swap_i = 0
    for i, num in enumerate(nums):
        if i <= s and nums[swap_i] < num:
            swap_i = i
    s -= swap_i
    answer.append(nums[swap_i])
    nums = nums[:swap_i] + nums[swap_i+1:]
print(*(answer+nums))
