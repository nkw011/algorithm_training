# https://programmers.co.kr/learn/courses/30/lessons/72410

# 연속문자 '.' 없애기
def convert_multiple_dot(s):
    not_dot = s.split('.')
    result = ''.join([w + '.' for w in not_dot if w != ''])
    if s[0] == '.':
        result = '.' + result
    if s[-1] != '.':
        result = result[:-1]
    return result


# 좌우 문자 '.' check
def check_dot(s):
    if s == '.':
        return ''
    if s[0] == '.':
        s = s[1:]
    if s[-1] == '.':
        s = s[:-1]
    return s


def solution(new_id):
    lower_id = ''
    for c in new_id:
        if c in '~!@#$%^&*()=+[{]}:?,<>/':
            continue
        if c.isupper():
            c = c.lower()
        lower_id += c
    lower_id = convert_multiple_dot(lower_id)
    lower_id = check_dot(lower_id)
    if lower_id == '':
        lower_id = 'a'
    if len(lower_id) > 15:
        lower_id = check_dot(lower_id[:15])
    if len(lower_id) <= 2:
        lower_id += (lower_id[-1] * (3 - len(lower_id)))
    return lower_id
