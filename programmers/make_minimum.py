# https://programmers.co.kr/learn/courses/30/lessons/12941
# '가장 작은 값 * 가장 큰 값, 가장 작은 값 * 가장 작은 값', 2개의 경우중 하나이다.

def solution(A,B):
    answer = 0
    for a,b in zip(sorted(A),sorted(B,reverse=True)):
        answer += a * b
    return answer
