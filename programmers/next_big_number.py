# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    nxt,cnt = n+1, bin(n).count('1')
    while True:
        if bin(nxt).count('1') == cnt:
            return nxt
        nxt += 1
