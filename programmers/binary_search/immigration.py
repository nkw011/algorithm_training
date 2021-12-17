# https://programmers.co.kr/learn/courses/30/lessons/43238
# 쉽게 간단하게 생각하자

def solution(n, times):
    max_time = max(times)
    answer = 0
    left,right = 1,(max_time * n)
    while left <= right:
        mid = (left+right) // 2
        cnt = sum([mid//t for t in times])
        if cnt >= n:
            answer = mid
            right = mid-1
        else:
            left = mid + 1
    return answer
