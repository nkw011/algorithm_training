# https://programmers.co.kr/learn/courses/30/lessons/64065

from collections import Counter
import re


def solution(s):
    s = eval(f"[{s[1:-1]}]")
    tuples = {len(numbers): numbers for numbers in s}
    result, contain = [], set()
    for t in range(1, len(tuples.keys())+1):
        for num in (tuples[t] - contain):
            result.append(num)
            contain.add(num)
    return result


# 참고 풀이 - 엄청난 풀이였다: 각 숫자를 counting한 이후 counting된 갯수가 많은 숫자부터 result에 포함된다.
def solution(s):
    s = Counter(re.findall('\d+', s))
    return [int(k) for k, v in sorted(s.items(), key=lambda x: -x[1])]
