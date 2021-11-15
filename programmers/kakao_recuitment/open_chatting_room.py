# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    user = {}
    for rec in record:
        r = rec.split(' ')
        if r[0] == 'Enter':
            user[r[1]] = r[2]
        elif r[0] == 'Change':
            user[r[1]] = r[2]
    result = []
    for rec in record:
        r = rec.split(' ')
        if r[0] == 'Enter':
            result.append(user[r[1]]+'님이 들어왔습니다.')
        elif r[0] == 'Leave':
            result.append(user[r[1]]+'님이 나갔습니다.')
    return result
