# # https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3)
    return str(int(''.join(numbers[::-1])))
