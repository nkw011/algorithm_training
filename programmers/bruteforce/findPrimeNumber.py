# https://programmers.co.kr/learn/courses/30/lessons/42839

import itertools
import math


def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for div in range(3, math.sqrt(num)+1, 2):
        if num % div == 0:
            return False
    return True


def solution(numbers):
    numbers = [num for num in numbers]
    ret = 0
    chk = [0] * (100000000)  # set을 이용해 중복 check하는 것이 더 메모리적으로 좋지않았을까?
    for leng in range(1, len(numbers)+1):
        for nums in itertools.permutations(numbers, leng):
            n = int("".join(nums))
            if not chk[n] and isPrime(n):
                chk[n] = 1
                ret += 1
    return ret
