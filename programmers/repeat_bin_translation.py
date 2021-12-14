# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    convert,zero_count = 0,0
    while s != '1':
        convert += 1
        zero_cnt = s.count('0')
        zero_count += zero_cnt
        s = bin(len(s) - zero_cnt)[2:]
    return [convert,zero_count]
