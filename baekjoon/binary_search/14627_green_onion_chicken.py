import sys
input = sys.stdin.readline

s,c = map(int,input().split())
onions = [int(input().rstrip()) for _ in range(s)]

result = 0
left = 1
# 해당하는 파에서 자르지 않고 그냥 다른 파에서 자를 수도 있다는 것을 왜 나는 생각하지 못했을까...??
right = max(onions)
sums = sum(onions)

while left <= right:
    mid = (left+right)//2
    count = 0
    for onion in onions:
        count += (onion // mid)
            
    if count >= c:
        left = mid +1
        result = max(result,mid)
    else :
        right = mid -1
        
# 남는 파 계산은 이런 식으로 편하게....
print(sums - (result * c))