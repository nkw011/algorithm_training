# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0
    max_n,min_n = max(a,b),min(a,b)
    while (max_n - min_n) != 1 or max_n % 2 or not min_n % 2:
        answer += 1
        max_n = max_n // 2 + 1 if max_n % 2 else max_n//2
        min_n = min_n // 2 + 1 if min_n % 2 else min_n // 2
    return answer + 1
