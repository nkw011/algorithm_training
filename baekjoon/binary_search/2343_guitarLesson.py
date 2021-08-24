import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lessons = list(map(int,input().split()))

left = 1
right = sum(lessons)
result = 0

while left <= right:
    mid = (left + right) //2
    count = 1
    blueray = 0
    for lesson in lessons:
        if blueray + lesson > mid :
            count += 1
            if lesson <= mid:
                blueray = lesson 
            else :
                # mid 값을 늘리기 위해 left = mid +1을 만들기 위해서 넣어줌
                count = m+1
                break
        else:
            blueray += lesson
    if count <= m:
        result = mid
        right = mid -1
    else :
        left = mid +1 
print(result)