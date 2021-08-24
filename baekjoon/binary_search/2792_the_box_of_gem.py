import sys
input = sys.stdin.readline

n,m = map(int,input().split())
gems = [int(input().rstrip()) for _ in range(m)]
gems.sort()

if n == 1:
    print(min(gems))
else :
    left = 0
    right = gems[m-1]
    result = gems[m-1]

    while left <= right:
        mid = (left+right) // 2
        count = 0
        possible = True
        for i in range(m):
            number = gems[i] // mid
            if gems[i] % mid != 0:
                number += 1
            if count + number > n:
                possible = False
                break
            else :
                count += number
        if not possible:
            left = mid +1
        else :
            right = mid -1
            result = min(result,mid)

    print(result)