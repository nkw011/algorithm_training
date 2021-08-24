import sys
input = sys.stdin.readline

def parametricSearch(limit):
    global n
    left = 1
    right = int(1e9)
    result, num = 0,0
    while left <= right:
        mid = (left+right) // 2
        num = (mid *(mid+1)) // 2
        
        if num <= n:
            left = mid+1
            result = max(result,mid)
        else :
            right = mid - 1
    return result

T = int(input().rstrip())
for loop in range(T):
    n = int(input().rstrip())
    print(parametricSearch(n))