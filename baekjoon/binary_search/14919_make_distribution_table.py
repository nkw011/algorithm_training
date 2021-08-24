import sys
import bisect
input = sys.stdin.readline

# 소수의 부동소수점 처리로 인해 정답이 잘 안나오는 것 같다...
def countByRange(left,right,array):
    l = bisect.bisect_left(array,left)
    r = bisect.bisect_left(array,right)
    
    return r - l


m = int(input().rstrip())
a = list(map(int,input().split()))
a.sort()

L = 1/m
left = 0
right = L

while right < 1:
    print(countByRange(left,right,a),end=" ")
    left = right
    right += L
print()