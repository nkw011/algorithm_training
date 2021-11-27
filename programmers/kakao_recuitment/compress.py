# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    d = {chr(ord('A')+idx-1): idx for idx in range(1, 27)}
    result = []
    i, leng, index = 0, len(msg), 27
    while i < leng:
        j = i+1
        while j <= leng and msg[i:j] in d.keys():
            j += 1
        result.append(d[msg[i:j-1]])
        d[msg[i:j]] = index
        index += 1
        i = j-1
    return result
