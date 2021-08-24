# 오름차순 내림차순 정렬 등에 관한 dp는 lis를 응용하면 된다는 것을 기억하자

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int,input().split()))
isExisted = [0] * (n+1)
length = [0] * (n+1)

isExisted[nums[0]] = 1
length[nums[0]] = 1

for i in range(1,n):
    if isExisted[nums[i]-1]:
        length[nums[i]] = length[nums[i]-1] +1
        isExisted[nums[i]] = 1
    else :
        isExisted[nums[i]] = 1
        length[nums[i]] = 1
        
print(n-max(length))