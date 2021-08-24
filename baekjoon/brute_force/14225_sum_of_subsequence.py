import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int,input().split()))
nums.sort()

result = nums[0]
if result != 1:
    print(1)
else :
    for i in range(2,n):
        if (result+1) != nums[i]:
            print(result)
            break
        else :
            result += nums[i]
    print(result+1)