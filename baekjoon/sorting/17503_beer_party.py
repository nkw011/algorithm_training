# sum 함수의 시간복잡도는 O(n)이다... 입력이 큰 문제일 수록 지양해야겠다.

import sys,heapq
input = sys.stdin.readline

n,m,k = map(int,input().split())
beers = [tuple(map(int,input().split())) for _ in range(k)]
beers = sorted(beers,key=lambda x:(x[1],x[0]))
likes = []
count = 0
possible = False
sums = 0
for i in range(k):
    now = beers[i][1]
    heapq.heappush(likes,beers[i][0])
    count += 1
    sums += beers[i][0]
    if count == n:
        if sums >= m:
            possible = True
            print(now)
            break
        else :
            sums -= heapq.heappop(likes)
            count -= 1
if not possible:
    print(-1)