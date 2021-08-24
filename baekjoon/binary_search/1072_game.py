#  z = (y/x)*100 으로 하면 답이 안나온다.
# z = int(y*100/x)처럼 y에 미리 100을 곱해야 값이 나온다.

import sys
input = sys.stdin.readline

x, y = map(int,input().split())
z = int(y*100/x)

left = 0
right = int(1e9)

if z >= 99:
    print(-1)
else :
    target = int(1e10)
    temp = 0

    while left <= right:
        mid = (left+right) // 2
        temp = int((y+mid)*100/(x+mid))

        if temp <= z:
            left = mid +1
        else:
            right = mid-1
            target = min(target,mid)
    print(target)