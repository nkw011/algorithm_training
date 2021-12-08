# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    progresses = [100-p for p in progresses]
    complete,answer = [],[]
    for a,b in zip(progresses,speeds):
        temp = a // b
        if a % b != 0: temp += 1
        complete.append(temp)
    s = complete[0]
    cnt = 1
    for c in complete[1:]:
        if c <= s:
            cnt += 1
        else:
            answer.append(cnt)
            s,cnt = c, 1
    answer.append(cnt)
    return answer
