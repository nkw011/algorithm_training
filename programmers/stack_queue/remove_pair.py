# https://programmers.co.kr/learn/courses/30/lessons/12973/solution_groups?language=python3&type=my
# 문자열 메소드 자체가 오래걸리기 때문에 시간 초과가 나오면 stack으로 비교하는 것이 좋은 것 같다.

def solution(s):
    if len(s) % 2: return 0
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if stack:
        return 0
    return 1
