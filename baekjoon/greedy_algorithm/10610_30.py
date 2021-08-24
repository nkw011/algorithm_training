import sys
input = sys.stdin.readline

def isThirtyMulti(nums):
    return nums.count(0) != 0 and sum(nums) % 3 == 0 

nums = list(map(int,input().rstrip()))
if not isThirtyMulti(nums):
    print(-1)
else :
    nums.sort(reverse=True)
    for i in nums :
        print(i,end="")
