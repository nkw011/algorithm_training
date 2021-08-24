import sys
input = lambda : sys.stdin.readline()

n = int(input())
town = [tuple(map(int,input().split())) for _ in range(n)]
town.sort(key=lambda x:(x[0],x[1]))
left = town[0][0]
right = town[n-1][0]
result = int(1e18)

while left <= right:
    mid = (left+right) // 2
    count = 0
    for dist,num in town:
        count += abs(dist-mid) * num
        
    if count <= result:
        result = count
        left = mid + 1
    else :
        right = mid -1
        
print(result)