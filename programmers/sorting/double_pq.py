# https://programmers.co.kr/learn/courses/30/lessons/42628#

def solution(operations):
    q = []
    for op in operations:
        o,num = op.split(" ")
        if o == 'I':
            q.append(int(num))
            q.sort()
        elif q and o == 'D' and num == '1':
            q.pop()
        elif q and o == 'D' and num == '-1':
            q = q[1:]
    if q:
        return [max(q),min(q)]
    return [0,0]
