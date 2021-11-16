# https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter
import re


# 첫번째 풀이
def solution(str1, str2):
    rex = re.compile('[a-zA-Z]{2}')
    counter_str1 = Counter([str1[i-1:i+1].lower()
                           for i in range(1, len(str1)) if rex.match(str1[i-1:i+1])])
    counter_str2 = Counter([str2[i-1:i+1].lower()
                           for i in range(1, len(str2)) if rex.match(str2[i-1:i+1])])
    n_intersect, n_union = 0, 0
    intersect = counter_str1.keys() & counter_str2.keys()
    for w in intersect:
        n_intersect += min(counter_str1[w], counter_str2[w])
        n_union += max(counter_str1[w], counter_str2[w])
    for w in counter_str1.keys():
        if w not in intersect:
            n_union += counter_str1[w]
    for w in counter_str2.keys():
        if w not in intersect:
            n_union += counter_str2[w]
    if n_union == 0:
        n_intersect, n_union = 1, 1
    return int((n_intersect / n_union) * 65536)


# 두번째 참고 풀이: union set을 만들어서 푼 것
def solution(str1, str2):
    rex = re.compile('[a-zA-Z]{2}')

    counter_str1 = Counter([str1[i-1:i+1].lower()
                           for i in range(1, len(str1)) if rex.match(str1[i-1:i+1])])
    counter_str2 = Counter([str2[i-1:i+1].lower()
                           for i in range(1, len(str2)) if rex.match(str2[i-1:i+1])])

    intersect = counter_str1.keys() & counter_str2.keys()
    union = counter_str1.keys() | counter_str2.keys()

    n_intersect = sum([min(counter_str1[w], counter_str2[w])
                      for w in intersect])
    n_union = 0
    for w in union:
        n1 = counter_str1[w] if w in counter_str1.keys() else 0
        n2 = counter_str2[w] if w in counter_str2.keys() else 0
        n_union += max(n1, n2)

    if n_union == 0:
        n_intersect, n_union = 1, 1

    return int(n_intersect/n_union * 65536)


# 세번째 참고 풀이: Counter 객체를 intersect, union 했을 때의 결과
def solution(str1, str2):
    rex = re.compile('[a-zA-Z]{2}')
    counter_str1 = Counter([str1[i-1:i+1].lower()
                           for i in range(1, len(str1)) if str1[i-1:i+1].isalpha()])
    counter_str2 = Counter([str2[i-1:i+1].lower()
                           for i in range(1, len(str2)) if str2[i-1:i+1].isalpha()])

    n_intersect = sum((counter_str1 & counter_str2).values())
    n_union = sum((counter_str1 | counter_str2).values())

    if n_union == 1:
        n_intersect, n_union = 1, 1
    return int(n_intersect / n_union * 65536)
