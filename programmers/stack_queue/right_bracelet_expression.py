# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    if len(s) % 2: return False
    for c in s[::-1]:
        if c == ')': stack.append(c)
        elif stack: stack.pop()
        else: return False
    return True
