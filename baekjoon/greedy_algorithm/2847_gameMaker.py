import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(n)]

count = 0
# 앞에서부터 하면 나중에 뒤로가다가 다시 앞을 고쳐야할 수도 있으므로
# 뒤에서부터 고치는 것이 핵심이다! -> 간단코드 원리
for i in range(n-1,0,-1):
    if nums[i] <= nums[i-1]:
        result = nums[i-1] - nums[i]
        count += (result + 1)
        nums[i-1] -= (result+1)

print(count)