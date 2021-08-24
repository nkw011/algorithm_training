import sys
import bisect
input = sys.stdin.readline

T = int(input().rstrip())
for loop in range(T):
    n,m = map(int,input().split())
    ns = list(map(int,input().split()))
    ms = list(map(int,input().split()))
    ns.sort()
    ms.sort()
    count = 0
    for number in ns:
        count += bisect.bisect_left(ms,number)
    print(count)