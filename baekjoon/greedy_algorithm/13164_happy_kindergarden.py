import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
diff = [(nums[i+1]-nums[i],i,i+1) for i in range(n-1)]
diff = sorted(diff, key = lambda x: (-x[0],-x[2]))
selected = [ diff[i][2] for i in range(k-1)]
selected.sort()

if k == 1:
    print(nums[n-1]-nums[0])
else :
    result = 0
    for i in range(k-1):
        index = selected[i]
        start = 0 if i == 0 else selected[i-1] 
        result += nums[index-1] - nums[start]
    result += nums[n-1] - nums[selected.pop()]
    print(result)