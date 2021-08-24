import sys,heapq
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for it in range(T):
    n = int(input())
    ret = 0
    nums = list(map(int,input().split()))
    heapq.heapify(nums)
    for _ in range(n-1):
        a,b = heapq.heappop(nums),heapq.heappop(nums)
        ret += (a+b)
        heapq.heappush(nums,a+b)
    print(ret)