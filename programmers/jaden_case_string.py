# https://programmers.co.kr/learn/courses/30/lessons/12951
# 문자열 built-in method인 capitalize의 활용

def solution(s):
    return " ".join([word.lower().capitalize() for word in s.split(" ")])
