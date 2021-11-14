# # https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    left, right = 0, citations[-1]
    while left <= right:
        mid = (left + right) // 2
        cnt = len([num for num in citations if num >= mid])
        if cnt >= mid:
            left = mid + 1
        else:
            right = mid-1
    return right
