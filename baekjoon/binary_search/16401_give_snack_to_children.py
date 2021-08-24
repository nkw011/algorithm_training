import sys
input = sys.stdin.readline

m,n = map(int,input().split())
snacks = list(map(int,input().split()))
snacks.sort()

left = 0
right = max(snacks)
result = 0

while left <= right:
    mid = (left+right) // 2
    count = 0
    for snack in snacks:
        count += (snack // mid)
    
    if count >= m:
        left += mid + 1
        result = max(result,mid)
    else :
        right = mid - 1
        
print(result)