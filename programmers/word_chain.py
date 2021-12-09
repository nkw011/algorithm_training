# https://programmers.co.kr/learn/courses/30/lessons/12981
from collections import defaultdict

def solution(n, words):
    p,t = -1,-1
    w_dict = defaultdict(int)
    pre = ''
    for idx, word in enumerate(words):
        w_dict[word] += 1
        if pre != '' and pre != word[0]:
            p,t = (idx % n) +1, (idx // n) + 1
            break
        if w_dict[word] >= 2:
            p,t = (idx % n) +1, (idx // n) + 1
            break
        pre = word[-1]
    if p != -1:
        return [p,t]
    return [0,0]
