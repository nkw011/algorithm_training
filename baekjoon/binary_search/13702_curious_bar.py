import sys
input = sys.stdin.readline

n,k = map(int,input().split())
waters = [int(input().rstrip()) for _ in range(n)]

left = 0
right = max(waters)
result = 0

while left <= right:
    mid = (left+right) // 2
    count = 0
    for water in waters:
        count += (water//mid)
    if count >= k:
        left = mid + 1
        result = max(result,mid)
    else :
        right = mid -1
        
print(result)