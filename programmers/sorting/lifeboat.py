# https://programmers.co.kr/learn/courses/30/lessons/42885
# 한 번에 2명만 탈 수있다는 사실을 보지못하고 계속 시간초과가 발생하였다.


def solution(people, limit):
    left,right,answer = 0,len(people)-1,0
    people.sort()
    while left <= right:
        answer += 1
        if people[left] + people[right] <= limit:
            left += 1
        right -=1
    return answer
