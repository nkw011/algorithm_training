import sys
input = sys.stdin.readline

def binarySearch(array,item):
    left = 0
    right = len(array)
    
    while left <= right:
        mid = (left+right) // 2
        if array[mid] == item:
            return 1
        elif array[mid] < item:
            left = mid+1
        else :
            right = mid-1
    return 0

T = int(input().rstrip())
for loop in range(T):
    n = int(input().rstrip())
    s1 = list(map(int,input().split()))
    s1.sort()
    m = int(input().rstrip())
    s2 = list(map(int,input().split()))
    s2.sort()
    for num in s2:
        print(binarySearch(s1,num))