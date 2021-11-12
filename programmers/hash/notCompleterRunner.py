# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(participant, completion):
    p1 = {}
    for p in participant:
        if p in p1.keys():
            p1[p] += 1
        else:
            p1[p] = 1
    for c in completion:
        p1[c] -= 1
    for p in p1.keys():
        if p1[p] != 0:
            return p
