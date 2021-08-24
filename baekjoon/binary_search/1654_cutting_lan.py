import sys
input = sys.stdin.readline

# 문제 조건에 자연수라고 명시가 되어있으니 이 점 주의하도록 하자

k,n = map(int,input().split())
length = [int(input().rstrip()) for _ in range(k)]
length.sort()
right = length[k-1]
left = 1
result = 0

while left <= right:
    mid = (left+right) // 2
    count = 0
    for l in length:
        count += (l//mid)
    if count >= n:
        left = mid +1
        result = mid
    else:
        right = mid -1
print(result)