# 최소 시간을 구하는 것이 parametric search의 목표로 하므로
# 그것을 바탕으로 구했다... 인원이 현재 목표인원보다 같거나 크면 result를 갱신해주고 right값을 낮췄다.
# 아니면 left 값을 올렸따...

import sys
input = lambda : sys.stdin.readline()

n,m = map(int,input().split())
tk = [int(input()) for _ in range(n)]
tk.sort()
left = tk[0]
right = tk[n-1] * m
result = 0
while left <= right:
    mid = (left+right) // 2
    count = 0 
    for t in tk:
        count += (mid // t)
        
    if count >= m:
        right = mid - 1
        result = count
    else :
        left = mid + 1
print(result)