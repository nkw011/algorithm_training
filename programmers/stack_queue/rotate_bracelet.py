# https://programmers.co.kr/learn/courses/30/lessons/76502

def matchBracelet(s):
    s2 = []
    while s:
        c = s.pop()
        if c == '}' or c == ']' or c == ')':
            s2.append(c)
        else:
            if not s2: return False
            c2 = s2.pop()
            if c == '{' and c2 != '}':
                return False
            if c == '(' and c2 != ')':
                return False
            if c == '[' and c2 != ']':
                return False
    return True

def solution(s):
    if len(s) % 2: return 0
    answer = 0
    s = list(s)
    for i in range(len(s)):
        if matchBracelet(s[i:]+s[:i]):
            answer += 1
    return answer
