# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for idx, ans in enumerate(answers):
        if p1[idx % 5] == ans:
            cnt[0] += 1
        if p2[idx % 8] == ans:
            cnt[1] += 1
        if p3[idx % 10] == ans:
            cnt[2] += 1
    maxValue = max(cnt)
    answer = [i+1 for i in range(3) if cnt[i] == maxValue]
    return answer


print(solution([1, 2, 3, 4, 5]))
