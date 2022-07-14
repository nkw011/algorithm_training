# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-2473
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-2473/


import sys
def input(): return sys.stdin.readline().rstrip()

def find_value(n, nums):
    result = [1e9,1e9,1e9]
    for i in range(n):
        l, r = i+1, n-1
        while l < r:
            # 세 수의 합이 0이 되는 것이 없을 경우를 대비해 0과 가장 가까운 세 수의 합을 찾아낸다.
            if abs(sum(result)) > abs(nums[i] + nums[l] + nums[r]):
                result = [nums[i], nums[l], nums[r]]

            if nums[i] + nums[l] + nums[r] == 0:
                return nums[i], nums[l], nums[r]
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
    return result[0], result[1], result[2]

n = int(input())
nums = list(map(int,input().split()))
nums.sort()

print(*find_value(n,nums))
