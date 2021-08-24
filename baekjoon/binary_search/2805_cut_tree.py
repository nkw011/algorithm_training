import sys
input = sys.stdin.readline

n, k = map(int,input().split())
trees = list(map(int,input().split()))

left = 0
right = max(trees)
result = 0
while left <= right:
    mid = (left + right) // 2
    remain = 0
    for length in trees:
        if length > mid:
            remain += (length - mid)
    if remain >= k:
        result = mid
        left = mid + 1
    else :
        right = mid -1
print(result)