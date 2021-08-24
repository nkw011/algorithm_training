# 정렬은 다양한 알고리즘에서 기본적으로 쓰이는 알고리즘으로
# 단순히 정렬만으로 모든 문제들을 풀 수 있다는 생각은 저버리자
# 이분 탐색이 나오면 먼저 파라메트릭 서치 알고리즘(Parametric Search)을 먼저 생각해보자...any()

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
levels = [int(input().rstrip()) for _ in range(n)]
levels.sort()
temp = 0
left = levels[0]
right = levels[0] + k
result = 0

while left <= right:
    mid = (left+right)//2
    possible = True
    for i in range(n):
        if levels[i] < mid:
            if temp + mid - levels[i] > k:
                possible = False
                break
            else :
                temp += (mid-levels[i])
        else:
            break
    
    if possible:
        left = mid+1
        result = mid
    else:
        right = mid - 1
    temp = 0
    
print(result)