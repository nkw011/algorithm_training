# 시작값을 최소 예산으로 하면 안 되고
# 최댓값을 정해진 예산으로 하면 오류가 난다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
moneys = list(map(int,input().split()))
m = int(input().rstrip())
maxValue = max(moneys)
sums = sum(moneys)

left = 0
right = m
target = 0

if sums <= m:
    print(maxValue)
else:
    while left <= right:
        mid = (left+right)//2
        result = 0
        for money in moneys:
            if money < mid:
                result += money
            else:
                result += mid
        if result <= m:
            left = mid+1
            target = max(target,mid)
        else:
            right = mid -1
            
    print(target)