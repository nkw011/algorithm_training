# https://programmers.co.kr/learn/courses/30/lessons/12899

# 몫과 나머지 124 국가 숫자를 잘 비교해보면 충분히 풀 수 있는 문제이다.
def solution(n):
    q = -1
    num_dict = {0:'4',1:'1',2:'2'}
    result = ''
    while q != 0:
        q = n // 3
        if n % 3 == 0:
            q -= 1
        result += num_dict[n%3]
        n = q
    return result[::-1]
