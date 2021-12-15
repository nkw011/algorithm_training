# https://programmers.co.kr/learn/courses/30/lessons/12953
# n개의 최소공배수를 구하는 방법은 앞에서부터 2개씩 최소공배수를 차례대로 구하면 된다.
# n개의 숫자의 최대공약수를 구해서 얻는 방법이 아니다.

from functools import reduce

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return (a * b) // gcd(a,b)

def solution(arr):
    return reduce(lcm,arr)
