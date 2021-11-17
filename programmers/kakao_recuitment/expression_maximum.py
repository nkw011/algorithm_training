# split을 어떻게 하면 더 잘 이용할 수 있을까에 대한 고민과
# 반복문을 어떻게 하면 다른 메소드로 바꿀 수 있을까에 대한 고민이 필요했던 문제

from itertools import permutations
from collections import deque
import re


def splitter(expression):
    rex1 = "[0-9]+"
    rex2 = "[\+|\-|\*]"
    nums = re.findall(rex1, expression)
    operands = re.findall(rex2, expression)
    exp = deque()
    for num, oper in zip(nums, operands):
        exp.append(num)
        exp.append(oper)
    exp.append(nums[-1])
    return exp


def solution(expression):
    maxValue = 0
    for operand in permutations(['*', '+', '-'], 3):
        exp = splitter(expression)
        for op in operand:
            stack = []
            while exp:
                c = exp.popleft()
                if c == op:
                    stack.append(str(eval(stack.pop() + c + exp.popleft())))
                else:
                    stack.append(c)
            exp = deque(stack)
        maxValue = max(maxValue, abs(int(exp[0])))
    return maxValue


# 차원이 다른 참고 풀이 : join의 참된 활용 / f문자열의 참된 사용 / 우선순위를 거꾸로 적용
def solution(expression):
    operands = list(permutations(['*', '-', '+']))
    maxValue = 0
    for op in operands:
        temp = []
        for exp in expression.split(op[0]):
            ex = [f"({i})" for i in exp.split(op[1])]
            temp.append(f"({op[1].join(ex)})")
        maxValue = max(maxValue, abs(eval(op[0].join(temp))))
    return maxValue
