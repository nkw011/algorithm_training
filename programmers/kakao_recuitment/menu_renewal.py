# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import defaultdict, Counter


# 첫번째 풀이
def solution(orders, course):
    new_course = defaultdict(list)
    for order in orders:
        order = sorted([c for c in order])
        total = len(order)
        for num in range(2, total+1):
            for arr in combinations(order, num):
                new_course[num].append(tuple(arr))
    result = []
    for num in course:
        if num in new_course.keys():
            count = Counter(new_course[num])
            maxValue = max(count.values())
            if maxValue >= 2:
                for order in count.keys():
                    if count[order] == maxValue:
                        result.append(''.join(order))
    return sorted(result)


# 두번째 참고 풀이: 문자열 정렬 리스트, Counter의 most_common() 메소드
def solution(orders, course):
    result = []
    for num in course:
        candidate = []
        for order in orders:
            for arr in combinations(sorted(order), num):
                candidate.append("".join(arr))
        most_common_cadidate = Counter(candidate).most_common()
        result += [k for k, v in most_common_cadidate if v >
                   1 and v == most_common_cadidate[0][1]]
    return sorted(result)
