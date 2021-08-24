import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int,input().split()))

idx1 = n-1
for i in range(n-1,-1,-1):
    if nums[i] < nums[i-1]:
        idx1 = i-1
        break
        
idx2 = n-1
for j in range(n-1,idx1,-1):
    if nums[j] < nums[idx1]:
        idx2 = j
        break
        
nums[idx1], nums[idx2] = nums[idx2],nums[idx1]
nums[idx1+1:] = sorted(nums[idx1+1:],reverse=True)

if n == 1 or idx1 == -1:
    print(-1)
else :
    for num in nums:
        print(num,end=" ")
    print()