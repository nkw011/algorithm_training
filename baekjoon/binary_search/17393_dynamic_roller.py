import bisect
import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


# python 리스트 슬라이스 (a[:])은 시간복잡도가 O(N)이라는 것을 알아두자
for i in range(n):
    number = bisect.bisect_right(b,a[i])
    number = number-(i+1) if number > i else 0
    print(number,end=" ")