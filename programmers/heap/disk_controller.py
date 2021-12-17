# https://programmers.co.kr/learn/courses/30/lessons/42627
# 생각을 최대한 단순하게...

import heapq

def solution(jobs):
    answer,now,cnt,n = 0,0,0,len(jobs)
    pre = 0
    q = []
    while cnt < n:
        for s,w in jobs:
            if pre <= s <= now:
                heapq.heappush(q,(w,s))
        if q:
            w,s = heapq.heappop(q)
            pre = now + 1
            now += w
            answer += (now-s)
            cnt += 1
        else:
            now += 1
    return answer // n
