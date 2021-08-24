import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int,input().split()))

if n == 1:
    print(sum(nums)-max(nums))
else :
    # 수가 항상 증가하는 수만 나올거라는 생각을 버리자 (주사위는 무조건 1 2 3 4 5 6이야 라는 편합한 생각을 버려야한다.)
    min1 = min(nums)
    min2 = int(1e9)
    min3 = int(1e9)
    
    for i in range(6):
        for j in range(6):
            if i != j and i+j != 5:
                if min2 > nums[i] + nums[j]:
                    min2 = nums[i] + nums[j]
    for i in [0,5]:
        for j in [1,4]:
            for k in range(2,4):
                min3 = min(min3,nums[i]+nums[j]+nums[k])
    
    total = 0
    total += ((5*n-6)*(n-2) * min1)
    total += ((8*n-12) * min2)
    total += (4 * min3)
    print(total)