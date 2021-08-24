import sys
input = sys.stdin.readline

def binarySearch(array,item):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == item:
            return 1
        elif array[mid] < item:
            left = mid+1
        else :
            right = mid -1
    return 0

n = int(input().rstrip())
nums = list(map(int,input().split()))
#이진 탐색은 정렬이 먼저 되어있어야한다.
nums.sort()

m = int(input().rstrip())
findNums = list(map(int,input().split()))

for find in findNums:
    print(binarySearch(nums,find),end=" ")