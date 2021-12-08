# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    f = heapq.heappop(scoville)
    cnt = 0
    while f < K:
        if not scoville: return -1
        s = heapq.heappop(scoville)
        heapq.heappush(scoville,(f+s*2))
        cnt += 1
        f = heapq.heappop(scoville)
    return cnt
