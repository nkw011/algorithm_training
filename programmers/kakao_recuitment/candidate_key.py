# https://programmers.co.kr/learn/courses/30/lessons/42890

from collections import Counter
from itertools import combinations


def solution(relation):
    row, col = len(relation), len(relation[0])
    candi_key = []
    for num in range(1, col+1):
        for arr in combinations(range(col), num):
            selected = ["".join([relation[r][col_num]
                                for col_num in arr]) for r in range(row)]
            count = Counter(selected)
            if len(count.keys()) == row:
                candi_key.append(arr)
    candi_key.sort(key=lambda x: len(x))
    result = set()
    for k in candi_key:
        can = True
        for num in range(1, len(k)+1):
            for arr in combinations(k, num):
                if arr in result:
                    can = False
        if can:
            result.add(k)
    return len(result)
