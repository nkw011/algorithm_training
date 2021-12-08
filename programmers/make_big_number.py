# https://programmers.co.kr/learn/courses/30/lessons/42883#

from collections import deque

def solution(number,k):
    answer = []
    # 뒷 수가 앞 수보다 작다고 빼는 것이 아니다. 뒷 수가 앞 수보다 클 때 앞 수를 빼내는 것이다.
    # 이 것을 착각하지말자
    for i,n in enumerate(number):
        while answer and k > 0 and answer[-1] < n:
            answer.pop()
            k -= 1
        if k == 0:
            answer.append(number[i:])
            break
        answer.append(n)
    # 마지막 테스트12가 for문을 지나고 나서도 k>0인 경우이다.
    # 이 때는 남은 수가 모두 같은 수이므로 뒤에서 k개를 제외한 나머지를 출력한다.
    if k > 0:
        return ("".join(answer))[:-k]
    return "".join(answer)
