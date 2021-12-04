# https://programmers.co.kr/learn/courses/30/lessons/64064

from itertools import product
import re
from collections import defaultdict


######################## 1번쩨 풀이 ##############################
# 테스트 5 〉	통과 (7270.33ms, 10.4MB)
def solution(user_id, banned_id):
    total = len(banned_id)
    case = defaultdict(int)

    def findCase(idx, result):
        if idx == total:
            if len(set(result)) == total:
                case[tuple(sorted(result))] += 1
            return
        for ids in candi_list[idx]:
            result.append(ids)
            findCase(idx+1, result)
            result.pop()

    candi_list = [[] for _ in range(total)]
    for b_id, candi in zip(banned_id, candi_list):
        reg = b_id.replace("*", ".")
        for user in user_id:
            if len(reg) == len(user) and re.match(reg, user):
                candi.append(user)
    findCase(0, [])
    print(case)
    return len(case)


######################## 2번쩨 풀이: 테스트 5번에서 제일 빠른 풀이 ##############################
# 테스트 5 〉	통과 (66.50ms, 10.3MB)
def solution(user_id, banned_id):
    total = len(banned_id)
    case = defaultdict(int)

    def findCase(idx, result):
        if idx == total:
            if len(result) == total:
                case[tuple(sorted(result.keys()))] += 1
            return
        for ids in candi_list[idx]:
            if ids not in result:
                result[ids] = 1
                findCase(idx+1, result)
                del result[ids]

    candi_list = [[] for _ in range(total)]
    for b_id, candi in zip(banned_id, candi_list):
        reg = b_id.replace("*", ".")
        for user in user_id:
            if len(reg) == len(user) and re.match(reg, user):
                candi.append(user)
    findCase(0, {})
    return len(case)


######################## 3번쩨 풀이 ##############################
# 테스트 5 〉	통과 (4997.63ms, 10.3MB)
def solution(user_id, banned_id):
    total = len(banned_id)
    case = defaultdict(int)

    candi_list = [[] for _ in range(total)]
    for b_id, candi in zip(banned_id, candi_list):
        reg = b_id.replace("*", ".")
        for user in user_id:
            if len(reg) == len(user) and re.match(reg, user):
                candi.append(user)

    for arr in product(*candi_list):
        if len(set(arr)) == total:
            case[tuple(sorted(arr))] += 1
    print(case)
    return len(case)
